# Resume Detail Extractor using AWS Textract

### Overview
This project is a **Resume Detail Extractor** built to extract specific information like **experience**, **education**, **email**, and **phone number** from resumes using **AWS Textract** for PDFs and **python-docx** for Word documents. 

The goal of this project is to learn **AWS Textract** and apply text processing using **regular expressions** (regex).

### Features
- Extracts text from PDF and Word resumes.
- Uses regex to extract:
  - **Email**
  - **Phone number**
  - **Experience**
  - **Education**
- Displays extracted information in a simple **Streamlit** UI.

### Why This Project
I completed this project to:
- Learn **AWS Textract**.
- Gain experience extracting structured information from unstructured data.
- Build a practical resume parsing tool.

### Technologies Used
- **AWS Textract** for extracting text from PDFs.
- **python-docx** for extracting text from Word documents.
- **Streamlit** for the user interface.
- **Regular Expressions (regex)** for extracting emails, phone numbers, experience, and education.

### How It Works
1. **Upload Resume**: Users can upload a resume in PDF or Word format.
2. **Text Extraction**:
   - PDFs: Processed using AWS Textract.
   - Word files: Processed using python-docx.
3. **Regex Extraction**: Extracts key details using regex patterns.
4. **Display Results**: The extracted information is displayed in the UI.

### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo-name/resume-extractor.git
   cd resume-extractor

### Install dependencies: Install the required libraries:

pip install streamlit pandas boto3 python-docx

### Run the Streamlit app

streamlit run app.py





<img width="786" alt="Screenshot 2024-10-23 at 3 25 30 PM" src="https://github.com/user-attachments/assets/8018ff82-f2f2-46db-8201-7eac0519a8bd">


