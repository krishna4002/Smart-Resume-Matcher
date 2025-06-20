# scripts/interview_gen.py

import os
import requests
from dotenv import load_dotenv

# --- Load Environment Variables ---
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")  # Store your key in .env

MODEL = "mistralai/mistral-7b-instruct:free"  # or try "openai/gpt-3.5-turbo" etc.

def generate_interview_questions(job_description):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"Generate 5 professional interview questions for a candidate applying to this job:\n\n{job_description}"

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert HR specialist."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    result = response.json()
    return result["choices"][0]["message"]["content"]