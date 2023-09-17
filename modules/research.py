import requests, os, dotenv, json
from PyPDF2 import PdfReader

dotenv.load_dotenv()
WORQHAT_API_KEY = os.getenv('WORQHAT_API_KEY')

def pdfRead(file):
    pdfFileObj = open(f'./files/{file}', 'rb')
    pdfReader = PdfReader(pdfFileObj)
    Content = ''.join([page.extract_text() for page in pdfReader.pages])
    pdfFileObj.close()
    Content = str(Content.encode('utf-8'))
    return Content

def summary(content):
    url = "https://api.worqhat.com/api/ai/content/v2"
    headers = {
        "Authorization": f"Bearer {WORQHAT_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "question" : f"""
        Your task is to generate a thorough summary of a research paper so that no important details are missing and a student can
        understand what the paper is trying to convey. The Content must be divided by the clearly marked Headings from the document,
        excluding the References section, and each section must be easily readable using bullet points.
    
        Summarize the Paper below with minimum one third length of original content, starting after the colon :
        
        {content}"""
    })
    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        return json.loads(response.text).get('content')
    except json.decoder.JSONDecodeError:
        return "There was an error getting this content."
    
    
def qna(content, question):
    url = "https://api.worqhat.com/api/ai/content/v2"
    headers = {
        "Authorization": f"Bearer {WORQHAT_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "question" : f"""
        Your task is to answer the given question after interpreting ONLY the given content.
    
        Question: {question}
        
        Content: {content}"""
    })
    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        return json.loads(response.text).get('content')
    except json.decoder.JSONDecodeError:
        return "There was an error getting this content."