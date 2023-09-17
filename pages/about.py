import streamlit as st
import home, navbar, about
# st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")

def render():
    st.title("Hi! There :wave:")
    st.markdown("<p style='font-size: 20px;'>Looks like you want to know about us</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Let me help you with that</p>", unsafe_allow_html=True)
    #about co-founders
    st.markdown("<p style='font-size: 20px;'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum consectetur cursus elit, non facilisis massa ultrices eu. Fusce sed dolor libero. Mauris pharetra feugiat\n nisl sit amet consequat. Proin tincidunt, augue at posuere facilisis, enim orci porttitor nisi, nec varius urna sapien at risus. Vivamus bibendum, sapien \nin semper vehicula, odio odio condimentum urna, nec fermentum urna metus a dolor. Pellentesque ac quam justo. Vestibulum sollicitudin enim nec dui suscipit, in laoreet elit mattis. </p>", unsafe_allow_html=True)
    #Services
    st.markdown("<p style='font-size: 30px; color: #87CEFA;'>The Services Provided By Us Are: </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Resource Searching</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Personalized Roadmap</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Research Paper Extraction/Summarization</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Grammar Correction</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Proctor Chatbot</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Notes Refinement Tool</p>", unsafe_allow_html=True)