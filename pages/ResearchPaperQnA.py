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

def qna(content, question):
    url = "https://api.worqhat.com/api/ai/content/v2"
    headers = {
        "Authorization": f"Bearer {os.getenv('WORQHAT_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "question" : f"""
        Your task is to answer the given question after interpreting ONLY the given content.
    
        Question: {question}
        
        Content: {content}"""
    })
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text
    

def main():
    pdf_docs = st.file_uploader("Upload", accept_multiple_files=True)
    user_question = st.text_input("Ask a Question...")
    if st.button("Process"):
        with st.spinner("Loading..."):
            raw_text = get_pdf_text(pdf_docs)
            st.write(raw_text)
            answer = qna(raw_text, user_question)
            print(answer)

main()