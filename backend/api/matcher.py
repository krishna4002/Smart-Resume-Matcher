from backend.services.embeddings import compute_similarity

def match_resume_to_job(resume_data, job_data):
    score = compute_similarity(resume_data['raw_text'], job_data['raw_text'])
    common_skills = set(resume_data['skills']) & set(job_data['skills_required'])
    missing_skills = set(job_data['skills_required']) - set(resume_data['skills'])
    return {
        "score": round(score * 100, 2),
        "matched_skills": list(common_skills),
        "missing_skills": list(missing_skills)
    }