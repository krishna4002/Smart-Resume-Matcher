import spacy
from backend.services.extractor import extract_text_from_file

nlp = spacy.load("en_core_web_sm")

def parse_resume(file_obj):
    text = extract_text_from_file(file_obj)
    doc = nlp(text)
    skills_keywords = ["python", "java", "c++", "docker", "flask", "tensorflow", "ml", "ai", "react", "node"]
    skills = [word.lower() for word in text.split() if word.lower() in skills_keywords]

    entities = {"name": "", "email": "", "phone": "", "skills": list(set(skills)), "raw_text": text}
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not entities["name"]:
            entities["name"] = ent.text
        elif ent.label_ == "EMAIL":
            entities["email"] = ent.text
        elif ent.label_ == "PHONE":
            entities["phone"] = ent.text
    return entities

def parse_job_description(text):
    doc = nlp(text.lower())
    skills_keywords = ["python", "java", "c++", "docker", "flask", "tensorflow", "ml", "ai", "react", "node"]
    skills = [word for word in skills_keywords if word in text.lower()]
    return {"skills_required": list(set(skills)), "raw_text": text}