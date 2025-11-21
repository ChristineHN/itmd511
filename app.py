# Course: ITMD-511
# Name: Hoa Le & Hyesoo Noh

# File: app.py

import streamlit as st
from api_util import (
    load_embedder,
    load_llm,
    compute_top_roles,
    call_coach_llm,
    continue_chat_with_history,
    calc_skill_match_percent
)
from career_db import CAREERS
from visualization import plot_skill_gaps, build_flow_dot
from sentence_transformers import util 


def is_on_topic(user_input, embedder):
    # 1) Quick keyword check (fast + avoids false negatives)
    CAREER_KEYWORDS = [
    # General work / experience
    "project", "projects", "workflow", "experience", "professional",
    "requirements", "documentation", "document", "operations",
    "process", "improve", "optimize", "support",

    # Team / collaboration
    "team", "stakeholder", "cross-functional", "collaboration",
    "coordinate", "communication", "meeting",

    # Technical / development
    "skills", "build", "built", "develop", "design", "implement",
    "analysis", "analyze", "testing", "debug", "app", "apps",
    "application", "software", "system", "automation", "work",

    # Data & tools
    "sql", "python", "tableau", "database",
    "report", "reporting", "dashboard", "data",

    # Business / BA / PM side
    "gather", "gathered", "requirement gathering",
    "process mapping", "workflow mapping", "use case",
    "business", "functional", "user story", "acceptance criteria",

    # Engineering / ops
    "manage", "managed", "operate", "operation", "deployment",
    "cloud", "infrastructure", "integration"
    ]

    lower_input = user_input.lower()
    if any(word in lower_input for word in CAREER_KEYWORDS):
        return True

    # 2) Embedding similarity check (fallback for subtle sentences)
    career_examples = [
        "career advice",
        "what job is right for me",
        "improve my skills",
        "I want to know my career direction",
        "find job roles that match me"
    ]
    user_emb = embedder.encode(user_input, convert_to_tensor=True)
    example_embs = embedder.encode(career_examples, convert_to_tensor=True)

    cosine_scores = util.cos_sim(user_emb, example_embs)
    max_score = float(cosine_scores.max())

    return max_score > 0.08



# === Page Setup ===
st.set_page_config(page_title="Career Path Coach", page_icon="🔎", layout="wide")


# === Model Loading ===
@st.cache_resource
def get_models():
    """Load and cache the embedding model and LLM."""
    embedder = load_embedder()
    llm = load_llm()
    return embedder, llm


embedder, llm = get_models()


# === Session State Initialization ===
if "history" not in st.session_state:
    st.session_state.history = [
        {
            "role": "assistant",
            "content": """
Hi! I'm your **AI Career Coach** 😊  
Tell me a bit about your **skills, experiences, or interests**, and I’ll help you discover  
the **top career paths** that match you.

Examples of what you can say:

> I analyze data using Python and SQL, and I've built dashboards using Tableau / Power BI to communicate insights. I’m interested in data-driven problem solving
>
> I’ve worked on building and maintaining web applications using JavaScript and Python. I also understand APIs, databases, and basic cloud deployment
>
> I worked on web applications using HTML, CSS, and JavaScript, and I’m comfortable structuring responsive layouts and reusable UI components.

When you're ready, just type about **what you’ve done or what you enjoy doing!**
"""
        }
    ]

if "conversation_mode" not in st.session_state:
    st.session_state.conversation_mode = "career"

if "top_roles" not in st.session_state:
    st.session_state.top_roles = []

if "chart_render_count" not in st.session_state:
    st.session_state.chart_render_count = 0

if "last_role_query" not in st.session_state:
    st.session_state.last_role_query = ""



# === Sidebar ===
with st.sidebar:
    st.markdown("### How this works")
    st.markdown("""
1. Describe your **skills, tools, or interests**
2. The system suggests **top 3 matching careers**
3. And provides **visual skill gaps and career progression**
    """)

    st.markdown("### Examples of useful info")
    st.markdown("""
- Tools you've used (Python, SQL, Figma, React, etc.)
- Projects you worked on
- Tasks you enjoy doing
    """)

    st.caption("Built with MiniLM embeddings + Gemma LLM")


# === Main UI ===
st.title("👩‍💻 Career Path Coach 👨‍💻")
st.caption("Personalized career guidance and visual insights.")


# === Render Chat History ===
for msg in st.session_state.history:
    if msg["content"] == "_charts_ready_":
        st.session_state.chart_render_count += 1 
        with st.chat_message("assistant"):
            if st.session_state.top_roles:
                # user_texts = [m["content"] for m in st.session_state.history if m["role"] == "user"]
                # last_user_input = user_texts[-1] if user_texts else ""
                last_user_input = st.session_state.last_role_query


                st.markdown("### Visual breakdown of your matches")

                for idx, (title, role, similarity_score) in enumerate(st.session_state.top_roles, start=1):
                    st.markdown(f"#### {idx}. {title}")
                    match_pct = calc_skill_match_percent(last_user_input, role["skills"])
                    st.write(f"**Skill match:** {match_pct}% | **Similarity score:** {similarity_score:.3f}")

                    try:
                        st.plotly_chart(
                            plot_skill_gaps(title, role["skills"], last_user_input),
                            use_container_width=True,
                            key=f"plot_{idx}_{st.session_state.chart_render_count}"
                        )

                    except Exception as e:
                        st.info(f"(skill chart unavailable: {e})")

                    try:
                        st.graphviz_chart(build_flow_dot(title, role["progression"]))
                    except Exception as e:
                        st.info(f"(progression diagram unavailable: {e})")

                st.markdown("---")
                st.markdown("""
                            ### 🔎 Understanding Similarity Scores
                            These similarity scores are based on a predefined set of 60 globally fast-growing careers 
                            (primarily within the technology, data, and healthcare domains). Please consult with a 
                            trusted advisor before making any decisions.

                            The similarity scores returned by the AI model can be interpreted as follows:

                            - **0.75-1.00**  → ✅ Excellent match  
                            - **0.50-0.74+** → ✅ Good match 
                            - **0.35–0.49**  → ✅ Moderate match  
                            - **Below 0.34** → ❌ Weak match  
                            """)

        continue  # Skip normal rendering

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)


# === Updated handle_user_input() with auto skill detection ===

def handle_user_input(user_input: str):
    """
    Process user input and generate career suggestions or continue chat.
    Behaviors:
    - If input is clearly about skills/tools/interests -> compute NEW top 3 careers + charts.
    - If input asks for charts -> show charts for latest results.
    - Otherwise -> continue conversational Q&A.
    """
    # 1️⃣ Off-topic guard
    if not is_on_topic(user_input, embedder):
        st.session_state.history.append({
            "role": "assistant",
            "content": """
I'm your **Career Coach** 😄  
I can help with:
- Skills you have
- Tools you've used
- Classes or projects you've done
- What kind of work you enjoy

Tell me something about **your background or interests**, and I’ll suggest careers that fit you!
"""
        })
        return

    # 2️⃣ Detect chart intent + skill-like content
    # Build a unified set of skill keywords from all careers
    all_skills = set()
    for role in CAREERS:
        for skill in role.get("skills", []):
            all_skills.add(skill.lower())

    user_text = user_input.lower()

    chart_keywords = ["chart", "visualize", "graph", "skill gap", "show me", "visualization"]
    wants_chart = any(k in user_text for k in chart_keywords)

    has_skill_info = any(skill in user_text for skill in all_skills)

    # 3️⃣ If user explicitly asks for charts and we have results -> show latest charts
    if wants_chart and st.session_state.top_roles:
        st.session_state.history.append({
            "role": "assistant",
            "content": "Here's your latest career match visualization."
        })
        st.session_state.history.append({"role": "assistant", "content": "_charts_ready_"})
        return

    # 4️⃣ If no clear skills in this message:
    #    - If we don't have any matches yet -> ask for more detail.
    #    - If we DO have matches -> treat as follow-up chat.
    if not has_skill_info:
        if not st.session_state.top_roles:
            st.session_state.history.append({
                "role": "assistant",
                "content": """
I want to recommend careers for you, but I need a bit more detail first 😊  
Could you share some **skills, tools, classes, or projects** you've worked with?

Examples:
- "I analyze data with SQL and Tableau."
- "I build web apps with React and APIs."
- "I worked with Python for automation scripts."
"""
            })
            return
        else:
            # Follow-up Q&A based on previous results
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    bot_reply = continue_chat_with_history(user_input, st.session_state.history, llm)
            st.session_state.history.append({"role": "assistant", "content": bot_reply})
            return

    # 5️⃣ If we reach here: user_input contains skill info (new or updated profile)
    #     → Always recompute top careers and show charts (even on later turns)
    top_roles_with_scores, _ = compute_top_roles(user_input, CAREERS, embedder, top_k=3)
    st.session_state.top_roles = [
        (role["title"], role, score) for role, score in top_roles_with_scores
    ]
    st.session_state.last_role_query = user_input
    st.session_state.conversation_mode = "chat"  # keep, but no longer blocks recompute

    with st.chat_message("assistant"):
        with st.spinner("Analyzing your strengths and career alignment..."):
            bot_reply = call_coach_llm(user_input, top_roles_with_scores, llm)

    st.session_state.history.append({"role": "assistant", "content": bot_reply})
    st.session_state.history.append({"role": "assistant", "content": "_charts_ready_"})



# === Chat Input ===
user_input = st.chat_input("Your turn...", key="main_chat_input")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    handle_user_input(user_input)
    st.rerun()