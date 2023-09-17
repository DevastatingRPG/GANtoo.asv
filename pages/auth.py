import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

url = "https://api.worqhat.com/authentication"

headers = {"Authorization": f"Bearer {os.getenv('WORQHAT_API_KEY')}"}

response = requests.request("POST", url, headers=headers)

print(response.text)