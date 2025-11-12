import re
from plotly.graph_objs._figure import Figure
from visualization import plot_skill_gaps, build_flow_dot
from api_util import compute_top_roles, calc_skill_match_percent


# ---- FR1: Skill Gap Chart Uses Exact Role Skills ----
def test_skill_gap_chart_exact_skill_match():
    role_skills = ["SQL", "Python", "Data Analysis"]
    user_text = "I know SQL and Python"
    
    fig = plot_skill_gaps("Data Analyst", role_skills, user_text)

    chart_skill_labels = fig.data[0].text  # labels printed in bars
    assert sorted(chart_skill_labels) == sorted(role_skills)
    assert len(chart_skill_labels) == len(role_skills)


# ---- FR2 + FR3: Similarity Computation & Top-3 Ranking ----
def test_compute_top_roles_similarity_and_top_three(monkeypatch):
    class FakeEmbedder:
        def encode(self, data, convert_to_tensor=True):
            return data  # skip actual embeddings

    def fake_cos_sim(user, careers):
        # Score = overlap in words
        def tokens(s): return set(re.findall(r"[a-zA-Z]+", s.lower()))
        u = tokens(user)
        scores = [len(u & tokens(c)) for c in careers]

        class FakeSim:
            def cpu(self): return self
            def tolist(self): return [scores]
        return FakeSim()

    import api_util
    monkeypatch.setattr(api_util.util, "cos_sim", fake_cos_sim)

    careers = [
        {"title": "Data Analyst", "description": "Analyze data using SQL", "skills": []},
        {"title": "ML Engineer", "description": "Build models using Python", "skills": []},
        {"title": "Business Analyst", "description": "Work with stakeholders", "skills": []},
        {"title": "Frontend Dev", "description": "Build UI using JavaScript", "skills": []},
    ]

    top, full = compute_top_roles("I use SQL for data analysis", careers, FakeEmbedder())

    assert len(top) == 3  # FR3
    scores = [score for _, score in top]
    assert scores == sorted(scores, reverse=True)  # FR2 ordering


# ---- FR4: Skill Gap Chart Must Be Generated ----
def test_skill_gap_chart_is_generated():
    fig = plot_skill_gaps("Data Analyst", ["SQL", "Excel"], "I know SQL")
    assert isinstance(fig, Figure)
    assert len(fig.data[0]["y"]) == 2  # one bar per skill


# ---- FR5: Career Progression Flowchart ----
def test_career_progression_flowchart_structure():
    progression = ["Junior Analyst", "Analyst", "Senior Analyst"]
    dot = build_flow_dot("Data Analyst", progression)

    assert "digraph" in dot
    assert 'node0 [label="You"' in dot
    assert "node0 -> node1" in dot
    assert "node1 -> node2" in dot


# ---- EXTRA TEST (supports FR1 + skill comparison correctness) ----
def test_calc_skill_match_percent_multi_word_skill():
    user_input = "I work with data analysis and python daily"
    skills = ["Data Analysis", "Python", "SQL"]
    
    percent = calc_skill_match_percent(user_input, skills)

    # "Data Analysis" and "Python" match, but not SQL → 2/3 = 66%
    assert percent == 67 or percent == 66  # rounding tolerance
