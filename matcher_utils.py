
import spacy
from io import BytesIO
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pdfminer.high_level import extract_text

# Load models
nlp = spacy.load("en_core_web_sm")
bert_model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text_from_pdf(uploaded_file):
    try:
        return extract_text(BytesIO(uploaded_file.read()))
    except Exception as e:
        return f"Error reading PDF: {e}"


def clean_text(text):
    doc = nlp(text)
    return " ".join([token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop])


def compute_tfidf_score(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(vectors[0:1], vectors[1:2])[0][0]


def get_bert_embedding(text):
    return bert_model.encode([text])[0]


def extract_keywords(text):
    doc = nlp(text)
    return set([token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop])


def compute_hybrid_score(resume_file, job_text, alpha=0.7):
    resume_raw = extract_text_from_pdf(resume_file)
    resume_clean = clean_text(resume_raw)
    job_clean = clean_text(job_text)

    if not resume_clean.strip() or not job_clean.strip():
        return 0.0, [], []

    bert_score = cosine_similarity(
        [get_bert_embedding(resume_clean)],
        [get_bert_embedding(job_clean)]
    )[0][0]

    tfidf_score = compute_tfidf_score(resume_clean, job_clean)
    final_score = alpha * bert_score + (1 - alpha) * tfidf_score

    # Keyword comparison
    resume_keywords = extract_keywords(resume_raw)
    job_keywords = extract_keywords(job_text)
    matched = list(resume_keywords & job_keywords)
    missing = list(job_keywords - resume_keywords)

    return round(final_score * 100, 2), matched, missing
