import streamlit as st
import module,aboutus
from streamlit_option_menu import option_menu
import pandas as pd

st.set_page_config(
    page_title= "Home",page_icon=":wave:"
)

st.title("Welcome Human!")
selected = option_menu(
    menu_title = None,
    options=["Home","Services","About Us"],
    icons = ["house","briefcase-fill","envelope"],       
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",    
    )

if selected == "Services":
    st.header("Services")
    select = option_menu(
        menu_title = None,
        options=["RP","Notes","Gen_P","GC","RR","QNA"],
        icons = ["alexa","card-text","file-earmark-ppt","book","journal-text","question-circle"],        
        menu_icon="cast",
        default_index=0,
        orientation="horizontal", 
        )
    if select == "RP":
        st.title("Research Paper :blue[Simplified]")
        pdf_docs = st.file_uploader("Upload", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Loading..."):
                raw_text = module.get_pdf_text(pdf_docs)
                output=module.summary(raw_text)
                st.write(output)

        
    if select == "Notes":
        st.title("Notes: :red[We Got Your Back]")
        pdf_docs = st.file_uploader("Upload", accept_multiple_files=False)     
        if st.button("Process"):
            with st.spinner("Loading..."):
                raw_text = module.pdfExtract(pdf_docs)
                sum = module.notes(raw_text)
                st.write(sum)
    
    if select == "QNA":
    # Initialize a session state variable to track if the warning has been shown
        if "show_warning" not in st.session_state:
            st.session_state.show_warning = True

        pdf_docs = st.file_uploader("Upload", accept_multiple_files=True)
        user_question = st.text_input("Ask a Question...")

        if pdf_docs is None or len(pdf_docs) == 0:
            if st.session_state.show_warning:
                st.write("Please upload a PDF document for specific answers.")

            if st.button("Process"):
                with st.spinner("Loading..."):
                    answer = module.qna1(user_question)
                    st.write(answer)
                    st.session_state.show_warning = False  # Set the warning state to False so it doesn't show again
        else:
            if st.button("Process"):
                with st.spinner("Loading..."):
                    raw_text = module.get_pdf_text(pdf_docs)
                    answer = module.qna(raw_text, user_question)
                    st.write(answer)
    
    if select == "Gen_P":
        st.title("PPT Content :blue[Generator]")
        topic = st.text_input("Enter a Topic")
        if st.button("Generate"):
            with st.spinner("Loading..."):
                ppt = module.ppt(topic)
                st.write(ppt)
                
    if select == "GC":
        st.title("Grammar :green[Checker]")
        text = st.text_area("Enter Text")
        if st.button("Check"):
            with st.spinner("Loading..."):
                out = module.GC(text)
                st.write(out)
     
    if select == "RR":
        st.title("Resource :blue[Recommendation]")
        text = st.text_input("Enter Text")
        if st.button("Check"):
            with st.spinner("Loading..."):
                nyt,yt = module.resource(text)
                data = [
                    nyt,
                    yt,
                ]
                transposed_data = list(zip(*data))
                column_names = ["Google","YouTube"]
                df = pd.DataFrame(transposed_data, columns=column_names)
                st.table(df.assign(hack='').set_index('hack'))
    
    
                   
if selected == "About Us":
    aboutus.aboutus()
    
    
if selected == "Login":
    pass


if selected == "Home":
     st.markdown("<p style='font-size: 80px; color: #87CEFA; text-align: center;'>GANtoo</p>",unsafe_allow_html=True)
     st.markdown("<h1 style='font-size: 50px; color: white; text-align: center;'>Bridging Classrooms, One Algorithm at a Time</h1>", unsafe_allow_html=True)


