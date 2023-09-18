import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    st.title("Grammar :green[Checker]")
    text = st.text_area("Enter Text")

    if st.button("Check"):
        with st.spinner("Loading..."):
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
            st.write(json.loads(response.text).get('content'))
            print(response.text)

main()