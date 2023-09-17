import streamlit as st
import requests
import json
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import os

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def main():
    load_dotenv()
    st.title("Research Paper :blue[Simplified]")
    pdf_docs = st.file_uploader("Upload", accept_multiple_files=True)
    if st.button("Process"):
        with st.spinner("Loading..."):
            raw_text = get_pdf_text(pdf_docs)
            url = "https://api.worqhat.com/api/ai/content/v2"

            headers = {
                "Authorization": f"Bearer {os.getenv('WORQHAT_API_KEY')}",
                "Content-Type": "application/json"
            }

            Content = str(str(raw_text).encode('utf-8'))
            payload = json.dumps({
                "question" : f"""
                Your task is to generate a thorough summary of a research paper so that no important details are missing and a student can
                understand what the paper is trying to convey. The Content must be divided by the clearly marked Headings from the document,
                excluding the References section, and each section must be easily readable using bullet points.
            
                Summarize the Paper below with minimum one third length of original content, starting after the colon :
                
                {Content}"""
            })

            response = requests.request("POST", url, data=payload, headers=headers)

            st.write(json.loads(response.text).get('content'))

main()