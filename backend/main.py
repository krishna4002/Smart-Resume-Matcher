from fastapi import FastAPI, UploadFile
from backend.api.parser import parse_resume, parse_job_description
from backend.api.matcher import match_resume_to_job
from backend.api.feedback import generate_feedback

app = FastAPI()

@app.post("/match")
async def match_endpoint(resume: UploadFile, jd: str):
    resume_data = parse_resume(resume.file)
    job_data = parse_job_description(jd)
    result = match_resume_to_job(resume_data, job_data)
    result["feedback"] = generate_feedback(result["missing_skills"])
    return result