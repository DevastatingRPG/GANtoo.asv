import streamlit as st
import home, navbar, about
def render():
    nav_options = ["Home", ":sparkles: Services", "About", "Login"]

    option = st.sidebar.radio("Navigate: ", nav_options)

    return option
