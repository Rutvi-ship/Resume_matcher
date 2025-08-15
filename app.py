# Import the Streamlit library for creating the web app
import streamlit as st

# Import helper functions from matcher_utils.py
# - extract_text_from_pdf: reads text from an uploaded PDF
# - compute_hybrid_score: calculates match score + matched/missing keywords
from matcher_utils import extract_text_from_pdf, compute_hybrid_score


# ------------------ PAGE CONFIGURATION ------------------

# Set the title of the browser tab and center the layout
st.set_page_config(page_title="Resume Matcher", layout="centered")

# Display the main title of the app at the top
st.title(" Resume Matcher with BERT + TF-IDF + Keyword Insights")

# Add a description telling the user what the app does
st.markdown("Upload your resume and paste a job description to get a match score and keyword analysis.")


# ------------------ USER INPUTS ------------------

# Create a file uploader for the user to upload their resume (PDF only)
resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

# Create a large text area where the user can paste the job description
job_description = st.text_area("Paste the Job Description")


# ------------------ MATCH BUTTON ------------------

# Create a button labeled "Match Now" — code below runs only when clicked
if st.button(" Match Now"):

    # Check if BOTH the resume file is uploaded and job description is not empty
    if resume_file and job_description.strip():

        # Show a spinner with the message "Analyzing..." while processing
        with st.spinner("Analyzing..."):

            # Call the hybrid score function to calculate:
            # - Match score (percentage)
            # - Matched keywords (present in both resume & job description)
            # - Missing keywords (present in job description but not in resume)
            score, matched_keywords, missing_keywords = compute_hybrid_score(resume_file, job_description)

            # Show the match score in a green success box
            st.success(f"Match Score: **{score}%**")

            # ------------- Matched Keywords Section -------------
            st.markdown("###  Matched Keywords:")  # Section title

            if matched_keywords:
                # Join all matched keywords with commas and display
                st.markdown(", ".join(matched_keywords))
            else:
                # If no keywords matched, show a placeholder message
                st.markdown("_No keywords matched._")

            # ------------- Missing Keywords Section -------------
            st.markdown("###  Missing Keywords (from Job Description):")  # Section title

            if missing_keywords:
                # Join all missing keywords with commas and display
                st.markdown(", ".join(missing_keywords))
            else:
                # If no keywords are missing, tell the user all are present
                st.markdown("_All important keywords are present._")

    else:
        # If resume or job description is missing, show a warning message
        st.warning(" Please upload a resume and paste the job description.")
