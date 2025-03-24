 AI Resume Screening and Candidate Ranking System  
Made with ❤️ using Python & Streamlit ✨  

📄 AI Resume Screening and Candidate Ranking System

 🚀 Problem Statement  
Identifying qualified candidates from a large pool of resumes is a complex and time-consuming task for recruiters. Manual screening is prone to errors, inconsistency, and bias, which can lead to the exclusion of deserving candidates. This system automates the resume screening and candidate ranking process to ensure efficient, fair, and accurate hiring decisions.

 🎯 Motivation  
- Reduce recruiter workload by automating resume screening.  
- Ensure deserving candidates are not overlooked due to resume inconsistencies.  
- Improve fairness and accuracy by ranking candidates based on job relevance.  

 🏆 Proposed Solution  
Our AI-powered resume screening system leverages **Natural Language Processing (NLP) and Machine Learning (ML) to:

✅ Extract skills, experience, and other essential qualifications from resumes.  
✅ Match candidate profiles with the job description.  
✅ Rank candidates based on relevance and present visual insights.  

---

 📂 Project Structure  
📂 AI-Resume-Screener/ 
├── 📄 app.py # Main Streamlit Application 
├── 📄 utils.py # Utility functions (text extraction, skill extraction, etc.) 
├── 📄 requirements.txt # Dependencies for the project 
├── 📄 install_dependencies.py # Script to install required packages 
├── 📂 resumes/ # Sample resumes (PDF/DOCX) 
└── 📄 README.md # Project documentation

🔧 Features  
✅ **Text Extraction** from resumes (PDF/DOCX).  
✅ **Skill Identification** using NLP and keyword matching.  
✅ **Experience Calculation** with advanced date parsing.  
✅ **Candidate Ranking** using TF-IDF and cosine similarity.  
✅ **Interactive Charts** for candidate visualization using Plotly.  
✅ **PDF Download** for the top-ranked candidate summary.  
✅ **Batch Processing** to handle multiple resumes simultaneously.  
✅ **User-Friendly Interface** with Streamlit.  

---
🛠️ Installation & Setup  

 1️⃣ Clone the Repository  

git clone https://github.com/ShrutiTate/AI-Resume-Screener.git
cd AI-Resume-Screener

2️⃣ Install Dependencies
Ensure you have Python installed (>= 3.8):
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

🌍 Deployment on Streamlit Cloud
Push the repository to GitHub:
git add .
git commit -m "Initial commit"
git push origin main
Go to Streamlit Cloud.
Click "New App", select your GitHub repository, and deploy!

🤝 Contribution Guidelines
We welcome contributions from the community! Follow these steps to contribute:

1.Fork the repository.
2.Create a new branch:git checkout -b feature-name
3.Make your changes and commit:git commit -m "Added a new feature"
4.Push the changes:git push origin feature-name
5.Open a Pull Request (PR) and describe your changes.

📜 License
This project is licensed under the MIT License. Feel free to use and enhance it.


