import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os
def main():
  load_dotenv()
  st.title("PPT Content :blue[Generator]")
  topic = st.text_input("Enter a Topic")
  if st.button("Generate"):
    with st.spinner("Loading..."):
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
      st.write(json.loads(response.text).get('content'))


main()