import streamlit as st
import pandas as pd
import boto3
from docx import Document
import re

# Textract client for extracting text from PDF
textract_client = boto3.client('textract')

# Function to extract resume content from PDF
def extract_resume_content(file):
    response = textract_client.analyze_document(
        Document={'Bytes': file.read()},
        FeatureTypes=["TABLES", "FORMS"]
    )

    extracted_text = ''
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_text += block['Text'] + '\n'
    return extracted_text

# Function to extract text from Word document (docx)
def extract_text_from_docx(file):
    doc = Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])

# Improved function to extract experience, education, email, and phone number using regex
def extract_resume_details(resume_text):
    # Regex patterns for email and phone number
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(\+?\d{1,4}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'

    # Experience pattern (looking for numeric and word-based years of experience)
    experience_pattern = r'(\d+|[oO]ne|[tT]wo|[tT]hree|[fF]our|[fF]ive|[sS]ix|[sS]even|[eE]ight|[nN]ine|[tT]en)\s+(years?|yrs?)\s+experience'

    # Education keywords and regex for degrees
    education_keywords = ['Bachelor', 'Master', 'PhD', 'B.Sc', 'M.Sc', 'Doctorate', 'Degree']
    education_pattern = r'(BS|BA|Bachelor|Master|PhD|B\.Sc|M\.Sc|Doctorate)\s+in\s+[A-Za-z\s]+'

    # Extracting details using regex
    email = re.findall(email_pattern, resume_text)
    phone_number = re.findall(phone_pattern, resume_text)
    experience = re.findall(experience_pattern, resume_text)

    # Extracting education by checking if certain keywords or patterns exist
    education = re.findall(education_pattern, resume_text)

    # Return the extracted information as a dictionary
    return {
        "email": email[0] if email else "Not Found",
        "phone_number": phone_number[0] if phone_number else "Not Found",
        "experience": f"{experience[0][0]} years" if experience else "Not Found",
        "education": education if education else ["Not Found"]
    }

# Streamlit UI for uploading resume and extracting details
def upload_and_extract_resume():
    st.title("Resume Detail Extractor")

    uploaded_file = st.file_uploader("Upload a resume (PDF/Word)", type=['pdf', 'docx'])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]

        if file_extension == 'pdf':
            resume_text = extract_resume_content(uploaded_file)
        else:
            resume_text = extract_text_from_docx(uploaded_file)

        # Display extracted resume text
        st.write("Extracted Resume Text:")
        st.text_area("", resume_text, height=200)

        # Extract specific details from the resume
        st.write("Extracting Details...")
        extracted_details = extract_resume_details(resume_text)

        # Display the extracted details in JSON format
        st.write("Extracted Resume Details:")
        st.json(extracted_details)

# Run the Streamlit app
if __name__ == '__main__':
    upload_and_extract_resume()
