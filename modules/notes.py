import requests, os, dotenv, json
from PyPDF2 import PdfReader
dotenv.load_dotenv()
SERP_API_KEY = os.getenv('SERP_API_KEY')
WORQHAT_API_KEY = os.getenv('WORQHAT_API_KEY')

def pdfExtract(pdfFile):  
  url = "https://api.worqhat.com/api/ai/v2/pdf-extract"
  headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {WORQHAT_API_KEY}'
  }
  files = {'file': pdfFile.getvalue()}
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
    and to the point. Wherever there is a mistake correct the mistake and return summarized correct content.  
    The Contents of the document start after the colon :
        
    {content}"""
  })
  response = requests.request("POST", url, data=payload, headers=headers)
  try:
      return json.loads(response.text).get('content')
  except json.decoder.JSONDecodeError:
      return "There was an error getting this content."


def resource(topic):
  url = "http://api.serpstack.com/search"
  params = {
    'access_key': SERP_API_KEY,
    'query': f'"{topic}" Tutorial -youtube'
  }
  alt = requests.request(url, params).json()
  params_yt = {
    'access_key': SERP_API_KEY,
    'query': f'"{topic}" Tutorial site: youtube.com'
  }
  yt = requests.request(url, params_yt).json()

  return [result['url'] for result in alt["organic_results"][:5]], [result['url'] for result in yt["organic_results"][:5]]
