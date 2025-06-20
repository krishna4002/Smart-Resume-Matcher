import streamlit as st
from backend.api.parser import parse_resume, parse_job_description
from backend.api.matcher import match_resume_to_job
from backend.api.feedback import generate_feedback
from backend.services.graph_recommender import recommend_career_paths
from backend.services.interview_gen import generate_interview_questions
from frontend.components.visualizations import show_skill_radar
from frontend.components.upload_resume import upload_resume_ui
from frontend.components.match_score import display_match_score

st.set_page_config("Resume Matcher", layout="wide")
st.title("🔍 Smart Resume Matcher")

col1, col2 = st.columns(2)
with col1:
    resume_file = upload_resume_ui()
with col2:
    job_text = st.text_area("Paste Job Description")

if resume_file and job_text:
    resume = parse_resume(resume_file)
    job = parse_job_description(job_text)
    result = match_resume_to_job(resume, job)

    display_match_score(result, resume)
    show_skill_radar(result['matched_skills'], result['missing_skills'])
    st.info(generate_feedback(result['missing_skills']))

    st.subheader("📌 Career Recommendations")
    for skill in result['matched_skills']:
        st.markdown(f"{skill.title()}** can lead to: {', '.join(recommend_career_paths(skill))}")

    st.subheader("🧠 Interview Questions")
    st.write(generate_interview_questions(job_text))