import fitz
import docx

def extract_text_from_file(file_obj):
    if file_obj.name.endswith(".pdf"):
        text = ""
        with fitz.open(stream=file_obj.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif file_obj.name.endswith(".docx"):
        document = docx.Document(file_obj)
        return "\n".join([para.text for para in document.paragraphs])
    return ""