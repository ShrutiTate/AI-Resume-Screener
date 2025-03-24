# utils.py
import fitz  # PyMuPDF
import docx
import re
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from PDF and DOCX files
def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    return "Unsupported file format."

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    return "".join(page.get_text() for page in doc)

def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    return "\n".join(para.text for para in doc.paragraphs)

# Extract skills (Simple Matching Approach)
def extract_skills(text):
    skills_db = ["python", "java", "machine learning", "deep learning", "nlp", "data analysis", "sql", "tensorflow", "pytorch"]
    extracted_skills = [skill for skill in skills_db if skill in text.lower()]
    return extracted_skills

# Improved experience calculation
def calculate_experience(text):
    # Match date ranges (e.g., Jan 2020 - Dec 2023, 2020-2023)
    date_patterns = [
        r"(\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d{4})\s*-\s*(\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d{4})",
        r"(\d{4})\s*-\s*(\d{4})"
    ]

    total_experience_months = 0

    for pattern in date_patterns:
        for start, end in re.findall(pattern, text):
            try:
                if len(start) == 4:  # Year only
                    start_date = datetime.strptime(start, "%Y")
                    end_date = datetime.strptime(end, "%Y")
                else:  # Month and Year
                    start_date = datetime.strptime(start, "%b %Y")
                    end_date = datetime.strptime(end, "%b %Y")

                # Ensure end date is not in the future
                end_date = min(end_date, datetime.today())

                if start_date < end_date:
                    total_experience_months += (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
            except ValueError:
                continue

    # Match explicit mentions (e.g., 3 years, 2 yrs)
    duration_pattern = re.compile(r"(\d+)\s*(?:years?|yrs?)")
    total_experience_months += sum(int(match) * 12 for match in duration_pattern.findall(text))

    # Return total experience in years
    return round(total_experience_months / 12, 1)

# Rank candidates based on job description
def rank_candidates(job_description, candidates):
    documents = [job_description] + candidates
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(documents)

    job_desc_vector = vectors[0]
    resume_vectors = vectors[1:]

    scores = cosine_similarity(job_desc_vector, resume_vectors).flatten()
    return scores * 100  # Convert to percentage

# Find missing skills from the job description
def find_missing_skills(job_description, resume_text):
    job_words = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())
    missing = job_words - resume_words
    return ", ".join(list(missing)[:10])
