# Course: ITMD-511
# Name: Hoa Le & Hyesoo Noh

# File: api_utils.py

import os, re
from sentence_transformers import SentenceTransformer, util
from huggingface_hub import InferenceClient

HF_TOKEN = os.getenv("HF_TOKEN")


def load_embedder():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def load_llm():
    model_id = "google/gemma-2-2b-it"
    return InferenceClient(model=model_id, token=HF_TOKEN)


def truncate_to_last_sentence(text: str) -> str:
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    if sentences and not text.strip().endswith(('.', '!', '?')):
        sentences = sentences[:-1]
    return ' '.join(sentences) if sentences else text


def compute_top_roles(user_input: str, careers: list, embedder, top_k: int = 3):
    user_emb = embedder.encode(user_input, convert_to_tensor=True)
    career_texts = [
        f"{c['title']}: {c['description']}. Skills: {', '.join(c['skills'])}"
        for c in careers
    ]
    career_embs = embedder.encode(career_texts, convert_to_tensor=True)
    sims = util.cos_sim(user_emb, career_embs).cpu().tolist()[0]
    scored = list(zip(careers, sims))
    scored_sorted = sorted(scored, key=lambda x: x[1], reverse=True)
    return scored_sorted[:top_k], scored_sorted


def call_coach_llm(user_input: str, top_roles_scored, llm):
    role_summaries = [
        f"- {r['title']}: {r['description']} (skills: {', '.join(r['skills'])})"
        for r, _ in top_roles_scored
    ]
    role_block = "\n".join(role_summaries)

    system_prompt = """
    You are a warm, structured career coach.
    Explain which careers fit the user and what to work on next.

    Formatting rules for Markdown:
    - Use **bold** for role names, not headers.
    - Start each role with a numbered list: "1. **Role Name**"
    - Each section title (e.g., **Why it fits:**, **Key Skills to Develop:**, **Certifications / Next Steps:**) must be on its own line, followed by its content on the next line.
    - Use bullet points (-) for lists of skills or next steps.
    - Leave one blank line between each numbered role.
    - Do NOT nest lists or mix bold and italics in the same line.
    - Always end sentences cleanly and logically.
    - Keep the entire response under 500 words.

    Example format:

    1. **Product Manager**

    **Why it fits:**
    You have strong communication and analytical skills that align well with this role.

    **Key Skills to Develop:**
    - Technical proficiency
    - Stakeholder management
    - Data analysis

    **Certifications / Next Steps:**
    - PMP certification
    - Agile methodology course

    End with one short, encouraging closing line.
    """

    user_prompt = f"""
    User said: "{user_input}"

    Top matching roles:
    {role_block}
    """

    try:
        response = llm.chat_completion(
            messages=[
                {"role": "system", "content": system_prompt.strip()},
                {"role": "user", "content": user_prompt.strip()}
            ],
            max_tokens=800,
            temperature=0.6,
            top_p=0.9
        )
        raw_text = response.choices[0].message.content
    except Exception:
        fallback_prompt = system_prompt + "\n\n" + user_prompt
        tg = llm.text_generation(fallback_prompt, max_new_tokens=800)
        raw_text = tg[0]["generated_text"] if isinstance(tg, list) else tg

    return truncate_to_last_sentence(raw_text)


def continue_chat_with_history(user_input, history, llm):
    messages = [{"role": "system", "content": "You are a friendly and helpful career coach."}]
    for msg in history[-5:]:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": user_input})

    try:
        response = llm.chat_completion(messages=messages, max_tokens=400, temperature=0.7, top_p=0.9)
        raw_text = response.choices[0].message.content
    except Exception:
        fallback_prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
        tg = llm.text_generation(fallback_prompt, max_new_tokens=400)
        raw_text = tg[0]["generated_text"] if isinstance(tg, list) else tg

    return truncate_to_last_sentence(raw_text)


def calc_skill_match_percent(user_input: str, career_skills: list):
    user_text = user_input.lower()
    user_tokens = set([t.strip().lower() for t in re.split(r"[,/;.\s]+", user_input)])

    match_count = 0
    for skill in career_skills:
        skill_l = skill.lower().strip()
        if skill_l in user_text:
            match_count += 1
        else:
            parts = skill_l.split()
            if all(p in user_tokens for p in parts):
                match_count += 1

    return round(100 * match_count / len(career_skills)) if career_skills else 0