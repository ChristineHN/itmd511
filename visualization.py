# Course: ITMD-511
# Name: Hoa Le & Hyesoo Noh

# File: visualization.py

# This function creates a Graphviz DOT string that Streamlit can use to display
# a career progression flowchart.
# *** ChatGPT-generated code ***
import re
import pandas as pd
import plotly.express as px


def plot_skill_gaps(career_title, career_skills, user_skills_text):
    """Improved: recognizes multi-word skills and partial matches."""
    user_text = user_skills_text.lower()
    user_tokens = set([t.strip().lower() for t in re.split(r"[,/;.\s]+", user_skills_text)])

    skill_gaps = {}
    for s in career_skills:
        s_lower = s.lower().strip()
        if s_lower in user_text or all(p in user_tokens for p in s_lower.split()):
            skill_gaps[s] = 1  # already has
        else:
            skill_gaps[s] = 2  # needs development

    df = pd.DataFrame([
        {"No.": i + 1, "Skill": k, "Gap": v}
        for i, (k, v) in enumerate(skill_gaps.items())
    ])

    fig = px.bar(
        df,
        x="Gap",
        y="No.",
        orientation="h",
        labels={
            "Gap": "Skill Values: 1 = Already has, 2 = Needs development",
            "No.": "Skill #"
        },
        title=f"Skill Gaps for {career_title}",
    )

    fig.update_traces(
        text=df["Skill"],
        textposition="inside",
        texttemplate="<b>%{text}</b>",
        insidetextanchor="middle",
        hovertemplate='Skill: %{text}<br>Value: %{x}<extra></extra>'
    )

    fig.update_yaxes(
        tickvals=df["No."],
        ticktext=df["No."].astype(str),
        autorange="reversed"
    )
    fig.update_xaxes(tickvals=[1, 2], range=[0, 3], dtick=1)
    fig.update_layout(showlegend=False, height=300, margin=dict(l=40, r=20, t=60, b=40))
    return fig


def build_flow_dot(career_title, progression_list):
    """Return Graphviz DOT diagram for career progression."""
    #nodes = [f'You ({career_title})'] + progression_list
    nodes = [f'You'] + progression_list
    dot = "digraph G {\n  rankdir=LR;\n"
    for i, node in enumerate(nodes):
        dot += f'  node{i} [label="{node}", shape=box, style=filled, fillcolor="#c9f2c7"];\n'
        if i > 0:
            dot += f'  node{i-1} -> node{i};\n'
    dot += "}"
    return dot