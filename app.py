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
Hi! I'm your **AI Career Coach** – tell me your **skills and interests**,  
and I'll recommend the **best-fitting career paths** for you.

For example, just say something like:

> "I build machine-learning models with Python, love data preprocessing, and write automation scripts."

> "I query data with SQL, create dashboards in Tableau, and enjoy pulling business insights."

> "I develop front-end apps with React and TypeScript, and I care about UX."

I'll then pick the **top 3 matching jobs** and explain:  
- **Why they fit you**  
- **Which skills to level up**  
- **Next steps / certifications**  

**Go ahead – share your skills or interests now!**
"""
        }
    ]

if "conversation_mode" not in st.session_state:
    st.session_state.conversation_mode = "career"

if "top_roles" not in st.session_state:
    st.session_state.top_roles = []


# === Sidebar ===
with st.sidebar:
    st.markdown("### How this works")
    st.markdown("""
1. **Tell me your skills or interests** (the more detail, the better!)  
2. I'll suggest **top 3 career matches**  
3. Say **"show charts"** or **"skill gaps"** to see visuals
    """)

    st.markdown("### Quick Tips")
    st.markdown("""
- Mention **tools**, **projects**, or **hobbies**  
- Use natural language  
- Say **"show me the chart"** anytime
    """)

    st.caption("Built with MiniLM embeddings + Gemma LLM")


# === Main UI ===
st.title("👩‍💻Career Path Coach👨‍💻")
st.caption("Personalized career guidance and visual insights.")


# === Render Chat History ===
for msg in st.session_state.history:
    if msg["content"] == "_charts_ready_":
        with st.chat_message("assistant"):
            if st.session_state.top_roles:
                # Get last user input
                user_texts = [m["content"] for m in st.session_state.history if m["role"] == "user"]
                last_user_input = user_texts[-1] if user_texts else ""

                st.markdown("### Visual breakdown of your matches")

                for idx, (title, role, similarity_score) in enumerate(st.session_state.top_roles, start=1):
                    st.markdown(f"#### {idx}. {title}")
                    match_pct = calc_skill_match_percent(last_user_input, role["skills"])
                    st.write(f"**Estimated skill match:** {match_pct}% | **Similarity score:** {similarity_score:.3f}")

                    # Skill gap chart
                    try:
                        st.plotly_chart(
                            plot_skill_gaps(title, role["skills"], last_user_input),
                            use_container_width=True
                        )
                    except Exception as e:
                        st.info(f"(skill chart unavailable: {e})")

                    # Career progression diagram
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

    # Render normal messages
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)


# === Handle User Input ===
def handle_user_input(user_input: str):
    """Process user input and generate appropriate response."""
    chart_keywords = ["chart", "visualize", "graph", "skill gap", "show me", "visualization"]
    wants_chart = any(k in user_input.lower() for k in chart_keywords)

    if st.session_state.conversation_mode == "career" and not wants_chart:
        top_roles_with_scores, _ = compute_top_roles(user_input, CAREERS, embedder, top_k=3)
        st.session_state.top_roles = [
            (role['title'], role, score) for role, score in top_roles_with_scores
        ]
        st.session_state.conversation_mode = "chat"

        bot_reply = call_coach_llm(user_input, top_roles_with_scores, llm)
        st.session_state.history.append({"role": "assistant", "content": bot_reply})
        st.session_state.history.append({"role": "assistant", "content": "_charts_ready_"})

    elif wants_chart and st.session_state.top_roles:
        st.session_state.history.append({
            "role": "assistant",
            "content": "Here's your latest career match visualization."
        })
        st.session_state.history.append({"role": "assistant", "content": "_charts_ready_"})

    else:
        bot_reply = continue_chat_with_history(user_input, st.session_state.history, llm)
        st.session_state.history.append({"role": "assistant", "content": bot_reply})


# === Chat Input ===
user_input = st.chat_input("Your turn...", key="main_chat_input")

if user_input:
    # Save and process user input
    st.session_state.history.append({"role": "user", "content": user_input})
    handle_user_input(user_input)
    st.rerun()