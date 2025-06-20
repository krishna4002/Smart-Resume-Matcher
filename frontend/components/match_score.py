import streamlit as st

def display_match_score(result, resume):
    st.subheader("Match Result")
    st.write(f"Candidate: {resume['name']}")
    st.write(f"Match Score: {result['score']}%")
    st.write(f"Matched Skills: {', '.join(result['matched_skills'])}")
    st.write(f"Missing Skills: {', '.join(result['missing_skills'])}")