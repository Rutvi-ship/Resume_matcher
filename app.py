import streamlit as st
from matcher_utils import extract_text_from_pdf, compute_hybrid_score

st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("📄 Resume Matcher with BERT + TF-IDF + Keyword Insights")
st.markdown("Upload your resume and paste a job description to get a match score and keyword analysis.")

resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])
job_description = st.text_area("Paste the Job Description")

if st.button("🔍 Match Now"):
    if resume_file and job_description.strip():
        with st.spinner("Analyzing..."):
            score, matched_keywords, missing_keywords = compute_hybrid_score(resume_file, job_description)

            st.success(f"✅ Match Score: **{score}%**")

            st.markdown("### ✅ Matched Keywords:")
            if matched_keywords:
                st.markdown(", ".join(matched_keywords))
            else:
                st.markdown("_No keywords matched._")

            st.markdown("### ❌ Missing Keywords (from Job Description):")
            if missing_keywords:
                st.markdown(", ".join(missing_keywords))
            else:
                st.markdown("_All important keywords are present._")
    else:
        st.warning("⚠️ Please upload a resume and paste the job description.")
