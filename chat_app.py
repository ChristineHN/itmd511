import streamlit as st
import json, os, re
from sentence_transformers import SentenceTransformer, util
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Career Coach", page_icon="👩🏻‍💻🧑🏻‍💻", layout="wide")

HF_TOKEN = os.getenv("HF_TOKEN")  

@st.cache_resource
def load_model():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

@st.cache_resource
def load_roles():
    with open("roles.json", "r") as f:
        return json.load(f)

@st.cache_resource
def load_client():
    model_id = "google/gemma-2-2b-it"  
    return InferenceClient(model=model_id, token=HF_TOKEN)

model = load_model()
roles = load_roles()
client = load_client()

st.title("Career Path Chatbot")
st.caption("Embedding-based role recommendations with natural language responses (MiniLM + Gemma-2-2B)")

if "history" not in st.session_state:
    st.session_state.history = [
        {"role": "assistant", "content": "Hey there! Tell me what you're into or what tech skills you have, and I’ll help you explore some fitting career paths."}
    ]

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# human authored code
def truncate_to_last_sentence(text):

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    if sentences and not text.endswith(('.', '!', '?')):
        sentences = sentences[:-1]
    return ' '.join(sentences) if sentences else text

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    user_emb = model.encode(user_input, convert_to_tensor=True)
    role_texts = [f"{r['title']}: {r['description']} {' '.join(r['core_skills'])}" for r in roles]
    role_embs = model.encode(role_texts, convert_to_tensor=True)
    sims = util.cos_sim(user_emb, role_embs).cpu().tolist()[0]
    top_roles = sorted(zip(roles, sims), key=lambda x: x[1], reverse=True)[:3]

    role_summary = "\n".join([f"{r['title']}: {r['description']}" for r, _ in top_roles])

    # --- Gemma-2-2B chat_completion ---
    #system_prompt = """You are a kind career coach. Provide a warm, detailed, and motivating response explaining why the recommended roles suit the user and suggest skills or certifications they could learn next. Keep it engaging and supportive, ensuring the response is complete within 300 tokens to avoid abrupt cutoff.."""
    # human authored code
    system_prompt = """You are a cynical but experienced career coach who has seen it all.
You care about helping the user, but you're blunt, sarcastic, and a little tired of people ignoring reality.
Give honest, detailed feedback about why the recommended roles fit them and what skills or certifications they should *actually* learn to survive in the field.
Keep it realistic, engaging, and slightly humorous—like a mentor who’s had too much coffee but still wants them to succeed.
Limit the response to around 1000 tokens.
"""

    user_prompt = f"""The user said: "{user_input}"

Based on their input, here are the most relevant tech roles:
{role_summary}

Respond with career advice tailored to their input."""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    with st.spinner("Generating response..."):
        try:
            # human authored code
            response = client.chat_completion(
                messages=messages,
                max_tokens=1000,
                temperature=0.7,
                top_p=0.9,
                stream=False
            )
            bot_reply = response.choices[0].message.content
            bot_reply = truncate_to_last_sentence(bot_reply)
        except Exception as e:
            bot_reply = f"Oops, something went wrong: {str(e)}. Try checking your HF_TOKEN or switching to 'Qwen/Qwen2-1.5B-Instruct'!"

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.history.append({"role": "assistant", "content": bot_reply})