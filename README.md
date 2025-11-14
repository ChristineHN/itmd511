
# Career Path Recommender — Prototype (Streamlit)

This is a lightweight prototype of a **Career Pathway Recommender** chatbot that suggests tech roles to a new grad, highlights skill gaps, and links resources.

## Stack
- Python + Streamlit (web UI)
- Simple in-repo catalog (`roles.json`) describing roles, skills

## Run locally
```bash
# 1) Run venv
source bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) Save your Hugging Face Token
cd .env
//enter HF_TOKEN=hf_your_actual_token_here

# 4) Launch
streamlit run app.py
```
