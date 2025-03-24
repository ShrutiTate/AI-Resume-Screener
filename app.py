# app.py
import streamlit as st
import pandas as pd
import os
from utils import extract_text, extract_skills, calculate_experience, rank_candidates, find_missing_skills
import plotly.express as px
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Set page configuration
st.set_page_config(page_title="AI Resume Screener", page_icon="📄", layout="wide")

st.title("🔍 AI Resume Screening & Candidate Ranking")

# Job Description Input
st.header("📌 Job Description")
job_description = st.text_area("Enter the job description")

# File Upload Section
st.header("📂 Upload Resumes")
uploaded_files = st.file_uploader("Upload resumes (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("📊 Ranked Candidates")

    resumes = []
    resume_names = []
    extracted_skills = []
    experiences = []

    for file in uploaded_files:
        text = extract_text(file)
        resumes.append(text)
        resume_names.append(file.name)
        extracted_skills.append(extract_skills(text))
        experiences.append(calculate_experience(text))

    scores = rank_candidates(job_description, resumes)

    # Normalize scores to a 0-100% range
    max_score = max(scores) if max(scores) > 0 else 1
    scores = [(score / max_score) * 100 for score in scores]

    missing_skills = [find_missing_skills(job_description, resume) for resume in resumes]

    results_df = pd.DataFrame({
        "Candidate": resume_names,
        "Skills": extracted_skills,
        "Experience (yrs)": experiences,
        "Missing Skills": missing_skills,
        "Similarity Score (%)": scores
    })
    results_df = results_df.sort_values(by="Similarity Score (%)", ascending=False).reset_index(drop=True)

    st.dataframe(results_df, use_container_width=True)

    # Interactive Chart with Plotly
    st.header("📊 Top 5 Candidates")
    fig = px.bar(results_df.head(5), x="Similarity Score (%)", y="Candidate", orientation='h', color="Experience (yrs)",
                 title="Top Candidates", hover_data=["Skills", "Missing Skills"], color_continuous_scale="Blues")
    st.plotly_chart(fig)

    # Download Resume as PDF
    st.header("📥 Download Top Resume")

    def create_pdf(content):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        story = [Paragraph(content.replace('\n', '<br/>'), styles['Normal'])]
        doc.build(story)
        buffer.seek(0)
        return buffer

    pdf_file = create_pdf(resumes[results_df.index[0]])

    st.download_button("Download Top Resume as PDF", pdf_file, file_name="top_resume.pdf", mime="application/pdf")