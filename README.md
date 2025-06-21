# 📄 Smart Resume Matcher

*Smart Resume Matcher* is an advanced AI-powered system designed to **automatically parse resumes**, **match them with job descriptions**, provide **personalized upskilling suggestions**, recommend **career growth paths** using **Neo4j knowledge graphs**, and even **generate interview questions** via Mistral (OpenRouter). All wrapped in an intuitive, user-friendly Streamlit interface backed by a powerful FastAPI engine.

---

## Who Is This For?

- HR professionals and recruiters
- Students looking to analyze their job-fit
- Job seekers aiming to improve their resumes
- Developers building intelligent recruitment systems
- Career counseling & job portals

---

## Features

| Feature                          | Description |
|----------------------------------|-------------|
| Resume Parser                 | Extracts name, email, phone, and tech skills from PDF/DOCX |
| Semantic Matcher              | Computes match score using SBERT sentence embeddings |
| Skill Insights               | Highlights matched and missing skills with feedback |
| Career Recommendations        | Uses Neo4j graph to suggest possible career paths |
| Interview Question Generator  | Uses Mistral model via OpenRouter to suggest 5 job-specific questions |
| Full UI & Backend Separation | FastAPI REST API + Streamlit Dashboard |
| Secure & Modular             | Easily extendable with new ML models or APIs |

---

## Project Structure

```
resume_matcher/
├── backend/
│   ├── api/                 # Resume & JD parsing, feedback logic
│   ├── services/            # Embeddings, text extraction, Neo4j queries, Interview generator
│   ├── models/              # Graph data (.cypher)
│   └── main.py              # FastAPI app
├── frontend/
│   ├── app.py               # Streamlit UI
│   └── components/          # Upload, charts, score display
├── scripts/                 # anonymizer
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/krishna4002/smart-resume-matcher.git
cd smart-resume-matcher
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install All Requirements
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## Running the Application

### 1. Start FastAPI Backend
```bash
uvicorn backend.main:app --reload
```
API available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2. Start Streamlit Frontend
In a new terminal:
```bash
streamlit run frontend/app.py
```
Access UI at: [http://localhost:8501](http://localhost:8501)

---

## Neo4j Career Graph Setup (Optional but Powerful)

### 1. Install [Neo4j Desktop](https://neo4j.com/download/)
Create a local database with username `neo4j`, password `test1234`.

### 2. Add Career Path Graph Data
Paste into Neo4j query editor:
```cypher
CREATE (s:Skill {name: "Python"})
CREATE (r:Career {name: "Data Scientist"})
CREATE (s)-[:LEADS_TO]->(r)
```
Add more skills and paths as needed.

### 3. Update your driver in graph_recommender.py
```python
GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "test1234"))
```

---

## 🤖 Interview Generator using Mistral (OpenRouter)

### 1. Get API Key from [https://openrouter.ai](https://openrouter.ai)
Paste it into scripts/interview_gen.py like this:
```python
headers = {
  "Authorization": "Bearer YOUR_API_KEY",
  "HTTP-Referer": "http://localhost"
}
```

### 2. Uses Mistral (free or paid) for 5 tailored questions likes:
> “What challenges have you faced with Python in data science projects?”

---

## Sample Use Case

- Candidate resume: Python, SQL, ML
- Job Description: Requires Python, NLP, SQL

→ **Output**:
- Match Score: 85%
- Matched Skills: Python, SQL
- Missing Skills: NLP
- Career Paths: Data Scientist, AI Engineer
- Feedback: “Consider upskilling in NLP”
- Interview Questions (Mistral AI): 5 generated questions

---

## Tech Stack

- Python 3.8+
- FastAPI (Backend)
- Streamlit (Frontend)
- spaCy (NER)
- SBERT (Sentence Embeddings)
- PyMuPDF + python-docx (Resume reading)
- Neo4j (Knowledge Graph)
- OpenRouter + Mistral (LLM API)

---

## Bonus Ideas to Expand

- Resume Anonymization tool
- Export interview questions to PDF
- JD builder using AI
- Fine-grained skill classification (using ESCO or O*NET)
- Multiple resume support (batch mode for HRs)

---

## Credits

- [spaCy](https://spacy.io/)
- [SentenceTransformers](https://www.sbert.net/)
- [Neo4j](https://neo4j.com/)
- [OpenRouter](https://openrouter.ai/)
- [Streamlit](https://streamlit.io/)
-
