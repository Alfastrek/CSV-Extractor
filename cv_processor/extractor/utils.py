import os
import re
import docx
from PyPDF2 import PdfReader

directory= os.path.join("cv_processor","static","cv_files")

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_info_from_cv(cv_file):
    file_ext = os.path.splitext(cv_file)[1].lower()
    if file_ext == ".pdf":
        text = extract_text_from_pdf(cv_file)
    elif file_ext == ".docx":
        text = extract_text_from_docx(cv_file)
    else:
        return None, None, None

    # Extract email and phone number using regex
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    return emails[0] if emails else None, phones[0] if phones else None, text

def process_cv_directory(directory):
    cv_info = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf") or filename.endswith(".docx"):
            cv_file = os.path.join(directory, filename)
            email, phone, text = extract_info_from_cv(cv_file)
            cv_info.append({"File": filename, "Email": email, "Phone": phone, "Text": text})
    return cv_info

