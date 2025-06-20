def generate_feedback(missing_skills):
    if not missing_skills:
        return "Great! You match all required skills."
    return f"Consider upskilling in: {', '.join(missing_skills)}"