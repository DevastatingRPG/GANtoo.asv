import requests, os, dotenv, json
from PyPDF2 import PdfReader

dotenv.load_dotenv()
WORQHAT_API_KEY = os.getenv('WORQHAT_API_KEY')
SERP_API_KEY = os.getenv('SERP_API_KEY')


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

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
    
def qna1(question):
    url = "https://api.worqhat.com/api/ai/content/v2"
    headers = {
        "Authorization": f"Bearer {WORQHAT_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "question" : f"""
        Your task is to answer the given question as far as you know.
        And if the question have mulitple answers just answer a bit of all the fields you can think of.
        And try give an appropriate heading to all if different answers. If the question is specific enough answer only that.
    
        Question: {question}
        
        Content: {""}"""
    })
    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        return json.loads(response.text).get('content')
    except json.decoder.JSONDecodeError:
        return "There was an error getting this content."
    
def pdfExtract(pdfFile):  
  with open("files/"+pdfFile.name, "wb") as f:
    f.write(pdfFile.getbuffer())
  url = "https://api.worqhat.com/api/ai/v2/pdf-extract"
  headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {WORQHAT_API_KEY}'
  }
  files=[
    ('file',(pdfFile.name,open("files/"+pdfFile.name,'rb'),'application/pdf'))
  ]
  response = requests.request("POST", url, headers=headers, files=files)
  content = json.loads(response.text).get('content')
  
  try:
    return content
  except json.decoder.JSONDecodeError:
    return "Error Reading this PDF"
        
def notes(content):
    url = "https://api.worqhat.com/api/ai/content/v2"
    headers = {
        "Authorization": f"Bearer {WORQHAT_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "question" : f"""
        Your task is to read a document containing Study Notes and make sure all the given info is accurate
        and to the point. Wherever there is a mistake correct the mistake and return correct content.
        Make sure the Code Section is properly formatted if the notes contain any code.  
        The Contents of the document start after the colon :
            
        {content}"""
    })
    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        return json.loads(response.text).get('content')
    except json.decoder.JSONDecodeError:
        return "There was an error getting this content."
    
    
def resource(topic):
    url = 'https://serpapi.com/search'
    params = {
        'api_key': SERP_API_KEY,
        'q': f'"{topic}" Tutorial -youtube'
    }
    alt = requests.get(url, params).json()
    params_yt = {
        'api_key': SERP_API_KEY,
        'q': f'"{topic}" Tutorial site: youtube.com'
    }
    yt = requests.get(url, params_yt).json()
    
    
    return [result['link'] for result in alt["organic_results"][:5]], [result['link'] for result in yt["organic_results"][:5]]

def ppt(topic):
    
            url = "https://api.worqhat.com/api/ai/content/v2"

            payload = json.dumps({
                "question": f"Your task is to generate content for each slide according to the title of the slide. YOu will not suggest anything to the user, you will generate actual content as if you are a student creating the ppt. Give the content in bullet points. The user will provide you with the topic: {topic}",
                "randomness": 0.4
            })
            headers = {
                'Content-Type': 'application/json',
                "Authorization": f"Bearer {os.getenv('WORQHAT_API_KEY')}",
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            return json.loads(response.text).get('content')
        
def GC(text):
    url = "https://api.worqhat.com/api/ai/content/v2"

    payload = json.dumps({
    "question": f"You are a grammar checker. Your task is to fix the grammar and the spelling mistakes of the user after the user inputs some text. You may also improve the creativity of the text given by the user to a certain extent. Divide the response into two sections: Corrected Grammar and Creative Improvement. The text given by the user is: {text}",
    "randomness": 0.2
})
    headers = {
    'Content-Type': 'application/json',
    "Authorization": f"Bearer {os.getenv('WORQHAT_API_KEY')}",
}

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text).get('content')