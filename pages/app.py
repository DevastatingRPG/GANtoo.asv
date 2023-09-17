import streamlit as st
import home, navbar, about

st.set_page_config(page_title="CollegeAI", page_icon=":robot_face:")


page = navbar.render()
if page == "Home":
    home.render()

if page == "About":
    about.render()




