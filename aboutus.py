import streamlit as st

def aboutus():
    st.title("Hi! There :wave:")
    st.markdown("<p style='font-size: 20px;'>Looks like you want to know about us</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Let me help you with that</p>", unsafe_allow_html=True)
    #about co-founders
    st.markdown("<p style='font-size: 20px;'>We aim to revolutionize remote learning by developing a system that curates personalized learning paths for students. Upon uploading their syllabus, students receive tailored resource recommendations, including video tutorials and reference websites. Recognizing the significance of research papers in academia, we have designed a feature to distill these dense documents into comprehensible summaries. Additionally, users can seek clarifications through a Q&A format based on the paper. Another offering, the 'Notes Reader,' permits students to upload class notes, which undergoes fact-checking and error removal, complemented by a concise summary for quick reviews.</p>", unsafe_allow_html=True)

    st.markdown("<p style='font-size: 20px;'>Future enhancements include comprehensive resource suggestions harnessing the YouTube API, backend functionalities for storing user interactions, and refining the Notes Reader to yield richer insights. The objective extends beyond students: our grammar checker aids in refining essays and emails, while our vision for a superior, automated PPT generator promises polished presentations, eliminating the need for further edits. Our overarching goal is to facilitate seamless remote education for all age groups while supporting educators </p>", unsafe_allow_html=True)
    #Services
    st.markdown("<p style='font-size: 30px; color: #87CEFA;'>The Services Provided By Us Are: </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Research Paper Summarization</p><p>- The co-founders of this site have streamlined research articles for you.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Notes</p><p>- Here, the co-founders have already done your resource research.</p> ", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>PPT Content Generation</p><p>- Using the specified input, this module creates the text for a PowerPoint presentation.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Grammar Checker</p><p>- This module both checks the text's grammar and offers a creative answer in conjunction with it.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Resource Recommendation</p><p>- Here, the co-founders have already done your resource research.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #90EE90;'>Question and Answer Section</p><p>- From the prompt or pdf(if provided), you are free to ask any query.</p>", unsafe_allow_html=True)