Resume Matcher: AI-Powered Job Matching

This project is a Streamlit-based application that evaluates how well a resume matches a given job description using a combination of:

-  **TF-IDF similarity**
-  **BERT sentence embeddings**
-  **Keyword extraction and comparison using spaCy**

---

## Features

- Upload your **resume (PDF)**
- Paste a **job description**
- Get a **hybrid match score** (combining BERT + TF-IDF)
- View:
  - Matched keywords between resume and job description
  -  Missing keywords from the job description

---

## 🧠 Technologies Used

| Tool | Purpose |
|------|---------|
| `streamlit` | Web UI |
| `sentence-transformers` | BERT-based sentence embeddings |
| `pdfminer.six` | PDF text extraction |
| `scikit-learn` | TF-IDF vectorization + cosine similarity |
| `spaCy` | Text cleaning and keyword extraction |
| `PyMuPDF` | (optional) for additional PDF handling |

---

## 📂 Folder Structure

resume_matcher_project/
│
├── app.py # Streamlit main app
├── matcher_utils.py # Backend utility functions
├── requirements.txt # Dependency list
└── README.md # You are here!



## 📦 Installation

```bash
# Step 1: Clone the repository
git clone https://github.com/your-username/resume-matcher.git
cd resume-matcher

# Step 2: Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # On Windows

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Download spaCy model
python -m spacy download en_core_web_sm


▶️ Run the App
streamlit run app.py


📝 How It Works

Resume text is extracted from uploaded PDF
Both resume and job description are cleaned and lemmatized using spaCy
Similarity is calculated using:
TF-IDF (cosine similarity)
BERT embeddings
A weighted average hybrid score is returned
Keywords are extracted from both texts and compared:


✅ Matched skills/keywords

❌ Missing ones from the resume

 Example Use Case

Perfect for job seekers who want to:

Tailor resumes before applying
Identify missing keywords in their resume
Improve chances of passing automated resume screeners (ATS)

 Author
Aayushi Patel
AI and Machine Learning Student, Cambrian College


