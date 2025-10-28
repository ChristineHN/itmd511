# Course: ITMD-511
# Name: Hoa Le & Hyesoo Noh

# File: app.py

# The main Streamlit application.
#Handles the user interface, input/output flow, and visualization of results.
#It connects user interactions with the core logic defined in the utility module.

import streamlit as st
from app_util import (
    load_embedder, load_llm,
    compute_top_roles, call_coach_llm,
    continue_chat_with_history, calc_skill_match_percent
)
from career_db import CAREERS
from visualization import plot_skill_gaps, build_flow_dot


# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Career Path Chatbot", page_icon="👩🏻‍💻", layout="wide")


# -----------------------------
# Model loading
# -----------------------------
@st.cache_resource
def get_models():
    """Cache model loading to avoid reloading on every rerun."""
    embedder = load_embedder()
    llm = load_llm()
    return embedder, llm


embedder, llm = get_models()


# -----------------------------
# Initialize session state
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = [
        {
            "role": "assistant",
            "content": "Hey 👋 Tell me your skills or interests, and I’ll suggest some career paths!"
        }
    ]

if "conversation_mode" not in st.session_state:
    st.session_state.conversation_mode = "career"

if "top_roles" not in st.session_state:
    st.session_state.top_roles = []


# -----------------------------
# Sidebar info
# -----------------------------
with st.sidebar:
    st.markdown("### How this works")
    st.markdown("""
1. Type what you know or enjoy doing.  
2. The model finds matching careers.  
3. You can later ask to **show charts** or **visualize skill gaps**.
    """)
    st.markdown("### Example inputs")
    st.markdown("""
- `I know Python, SQL, and like backend systems.`  
- `I’m interested in data analysis.`  
- `Show me my skill gap chart.`
    """)
    st.caption("Built with MiniLM embeddings + Gemma LLM 💬")


# -----------------------------
# Chat rendering
# -----------------------------
st.title("Career Path Chatbot 👩🏻‍💻🧑🏻‍💻")
st.caption("Personalized career guidance and visual insights.")

for msg in st.session_state.history:
    if msg["content"] == "_charts_ready_":
        # Display charts only when explicitly requested
        if st.session_state.top_roles:
            user_texts = [m["content"] for m in st.session_state.history if m["role"] == "user"]
            last_user_input = user_texts[-1] if user_texts else ""

            st.markdown("---")
            st.markdown("### Visual breakdown of your matches")

            for idx, (role, score) in enumerate(st.session_state.top_roles, start=1):
                st.markdown(f"#### {idx}. {role['title']}")
                match_pct = calc_skill_match_percent(last_user_input, role["skills"])
                st.write(f"**Estimated skill match:** {match_pct}%")

                try:
                    st.plotly_chart(
                        plot_skill_gaps(role["title"], role["skills"], last_user_input),
                        use_container_width=True
                    )
                except Exception as e:
                    st.info(f"(skill chart unavailable: {e})")

                try:
                    st.graphviz_chart(build_flow_dot(role["title"], role["progression"]))
                except Exception as e:
                    st.info(f"(progression diagram unavailable: {e})")

                st.markdown("---")
        continue

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)


# -----------------------------
# Input handler
# -----------------------------
def handle_user_input(user_input: str):
    """Process user input and update chat + visuals accordingly."""
    chart_keywords = ["chart", "visualize", "graph", "skill gap", "show me"]
    wants_chart = any(k in user_input.lower() for k in chart_keywords)

    if st.session_state.conversation_mode == "career" and not wants_chart:
        top_roles, _ = compute_top_roles(user_input, CAREERS, embedder, top_k=3)
        st.session_state.top_roles = top_roles
        st.session_state.conversation_mode = "chat"

        bot_reply = call_coach_llm(user_input, top_roles, llm)
        st.session_state.history.append({"role": "assistant", "content": bot_reply})
        st.session_state.history.append({"role": "assistant", "content": "_charts_ready_"})

    elif wants_chart and st.session_state.top_roles:
        st.session_state.history.append({
            "role": "assistant",
            "content": "Here’s your latest career match visualization."
        })
        st.session_state.history.append({"role": "assistant", "content": "_charts_ready_"})

    else:
        bot_reply = continue_chat_with_history(user_input, st.session_state.history, llm)
        st.session_state.history.append({"role": "assistant", "content": bot_reply})


# -----------------------------
# Chat input
# -----------------------------
user_input = st.chat_input("Your turn...", key="main_chat_input")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    handle_user_input(user_input)
    st.rerun()
