import streamlit as st

def upload_resume_ui():
    return st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])