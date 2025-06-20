import spacy

def anonymize_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "EMAIL", "PHONE", "GPE"]:
            text = text.replace(ent.text, f"<{ent.label_}>")
    return text