from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import pdfplumber
import google.generativeai as genai

# Configure the Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to call the Gemini model and generate a response based on the job description and resume content
def get_gemini_response(input, resume_text, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Use the newer Gemini model
    response = model.generate_content([input, resume_text, prompt])  # Generate the response based on inputs
    return response.text

# Function to extract text from the uploaded resume PDF
def extract_text_from_pdf(uploaded_file):
    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
    else:
        raise FileNotFoundError("No file uploaded")  # generate error if no file is uploaded

# Streamlit App
st.set_page_config(
    page_title="Job Matching and Candidate Analysis Expert System ",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #00b4d8, #ff7f50);
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTextInput, .stFileUploader, .stTextArea {
        border: 1px solid #cccccc !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    .stButton button {
        background-color: #007BFF !important;
        color: white !important;
        font-size: 16px !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        border: none !important;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton button:hover {
        background-color: #0056b3 !important;
    }
    .header-title {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="header-title">📄 Job Matching and Candidate Analysis System </h1>', unsafe_allow_html=True)
st.markdown("""Welcome to the Job Matching and Candidate Analysis Expert! This tool helps you enhance the recruitment process by automating the alignment of resumes with job requirements and evaluating interview content.""")

# Input field for job description
st.markdown("### Job Description:")
input_text = st.text_area(
    "Paste the job description below: ",
    key="input",
    placeholder="E.g., Looking for a Data Scientist with expertise in Python, machine learning, and data visualization.",
)

# File uploader for resume (PDF)
st.markdown("### Upload Your Resume:")
uploaded_file = st.file_uploader("Upload your resume (PDF format only)", type=["pdf"])
if uploaded_file is not None:
    st.success("PDF Uploaded Successfully!")

# **Video upload section added here**:
st.markdown("### Upload a Video:")
uploaded_video = st.file_uploader("Upload a video (MP4 format only)", type=["mp4"])

if uploaded_video is not None:
    st.success("Video Uploaded Successfully!")
    # Display the uploaded video
    st.video(uploaded_video)

# Buttons with spacing
st.markdown("### Actions:")
col1, col2 = st.columns(2, gap="large")

with col1:
    submit1 = st.button("🔍 Analyze Resume")
with col2:
    submit3 = st.button("📊 Match Percentage")

# Prompt templates for different use cases
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as a percentage, then keywords missing, and last, final thoughts.
"""

# Output Section
st.markdown("---")
st.markdown("### Results:")

if submit1:
    if uploaded_file is not None:
        # Extract text from the uploaded PDF
        try:
            resume_text = extract_text_from_pdf(uploaded_file)
            response = get_gemini_response(input_prompt1, resume_text, input_text)
            st.success("Resume Analysis Complete!")
            st.write(response)
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    else:
        st.warning("Please upload your resume first!")

elif submit3:
    if uploaded_file is not None:
        # Extract text from the uploaded PDF
        try:
            resume_text = extract_text_from_pdf(uploaded_file)
            response = get_gemini_response(input_prompt3, resume_text, input_text)
            st.success("Match Percentage Calculated!")
            st.write(response)
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    else:
        st.warning("Please upload your resume first!")
