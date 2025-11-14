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


def enforce_section_spacing(text: str) -> str:
    """
    Post-format the LLM output so that:
    - A/B/C headers are on their own line with a blank line after each header.
    - There is a blank line between sections and between careers.
    """
    import re
    t = text

    # Ensure a blank line BEFORE B. and C. (so A and B don't run together)
    t = re.sub(r'\nB\.\s*\*\*Key Skills Needed:\*\*', r'\n\nB. **Key Skills Needed:**', t, flags=re.IGNORECASE)
    t = re.sub(r'\nC\.\s*\*\*Next Steps\*\*:?', r'\n\nC. **Next Steps:**', t, flags=re.IGNORECASE)

    # Ensure headers are followed by ONE blank line (header on its own line)
    t = re.sub(r'(A\. \*\*Why it fits:\*\*)[ \t]*\n?', r'\1\n\n', t)
    t = re.sub(r'(B\. \*\*Key Skills Needed:\*\*)[ \t]*\n?', r'\1\n\n', t)
    t = re.sub(r'(C\. \*\*Next Steps:\*\*)[ \t]*\n?', r'\1\n\n', t)

    # Ensure a blank line between careers (lines starting with "1. **", "2. **", etc.)
    t = re.sub(r'\n(?=\d+\.\s\*\*)', r'\n\n', t)

    # Collapse excessive blank lines to double newlines
    t = re.sub(r'\n{3,}', '\n\n', t)

    return t.strip()



def call_coach_llm(user_input: str, top_roles_scored, llm):
    # Build detailed summaries of top roles (with skills list)
    role_summaries = []
    for idx, (r, score) in enumerate(top_roles_scored, start=1):
        skills_str = ", ".join(r.get("skills", []))
        summary = (
            f"{idx}. **{r['title']}**\n"
            f"   Description: {r.get('description','')}\n"
            f"   Skills: {skills_str}\n"
            f"   Similarity Score: {score:.3f}\n"
        )
        role_summaries.append(summary)
    role_block = "\n\n".join(role_summaries)

    # === SYSTEM PROMPT ===
    system_prompt = """
You are a warm, structured career coach.

STRICT FORMATTING RULES:
- For each career, output EXACTLY these sections in this order.
- Each SECTION HEADER must be indented with a tab on its own line, followed by ONE BLANK LINE, then the content.
- Put ONE BLANK LINE between sections. Put ONE BLANK LINE between careers.
- Do NOT place a header and its content on the same line.

Section headers (use these verbatim):
    A. **Why it fits:**
    B. **Key Skills Needed:**
    C. **Next Steps:**

Content rules:
- “Key Skills Needed” must be a bullet list using only the provided skills (one skill per line, starting with "- ").
- “Next Steps” must be 2–5 short, actionable bullets starting with a strong verb.
- Do NOT invent skills. Keep total under 500 words.
- Must end the entire reply with ONE short, encouraging closing sentence on its own line.

Example shape (spacing matters):

<insert new line>

1. **Role Name**

    A. **Why it fits:**

    [Explain why this career fits the user’s background, skills, and interests.]
          
    <insert a new line between A. and B.>

    B. **Key Skills Needed:**

    - Skill 1
    - Skill 2
    - Skill 3

    <insert a new line between B. and C.>

    C. **Next Steps:**

    - Do X
    - Practice Y
    - Learn Z

    <insert a new line after C.>

""".strip()

    # === USER PROMPT ===
    user_prompt = f"""
The user said: "{user_input}"

Top-matching careers with their real skills:
{role_block}

Write the response for the TOP 3 careers following the exact formatting rules above.
Use the skills exactly as provided for “Key Skills Needed.”
End with one separate encouraging closing line.
""".strip()

    # --- Primary attempt (chat) ---
    try:
        response = llm.chat_completion(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=900,
            temperature=0.0,  # deterministic
            top_p=1.0
        )
        raw_text = response.choices[0].message.content
        formatted = enforce_section_spacing(raw_text)
        return truncate_to_last_sentence(formatted)

    # --- Fallback (still chat_completion) ---
    except Exception:
        try:
            response = llm.chat_completion(
                messages=[
                    {"role": "system", "content": "You are a concise, structured career coach. Follow the formatting rules exactly."},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=900,
                temperature=0.0,
                top_p=1.0
            )
            raw_text = response.choices[0].message.content
            formatted = enforce_section_spacing(raw_text)
            return truncate_to_last_sentence(formatted)
        except Exception:
            return "I couldn’t reach the model to explain the matches. Please try again."



def continue_chat_with_history(user_input, history, llm):
    messages = [{"role": "system", "content": "You are a friendly and helpful career coach."}]
    for msg in history[-5:]:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": user_input})

    # Primary attempt (chat)
    try:
        response = llm.chat_completion(
            messages=messages,
            max_tokens=400,
            temperature=0.0,   # deterministic
            top_p=1.0
        )
        raw_text = response.choices[0].message.content
        return truncate_to_last_sentence(raw_text)
    except Exception:
        # Fallback: still chat_completion (NOT text_generation)
        try:
            fallback_prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
            response = llm.chat_completion(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Continue the conversation briefly and helpfully."},
                    {"role": "user", "content": fallback_prompt}
                ],
                max_tokens=400,
                temperature=0.0,
                top_p=1.0
            )
            raw_text = response.choices[0].message.content
            return truncate_to_last_sentence(raw_text)
        except Exception:
            return "I couldn’t reach the model to continue the chat. Please try again."



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