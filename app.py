import streamlit as st
from utils.wiki import get_summary
from utils.converter import text_to_audio, text_to_pdf

st.title("📚 Wikipedia Assistant")

keyword = st.text_input("Enter topic")

if st.button("Search"):
    summary, error = get_summary(keyword)

    if not error:
        st.session_state["summary"] = summary

if "summary" in st.session_state:

    st.write(st.session_state["summary"])

    option = st.radio("Choose format", ["Audio", "PDF"])

    file_name = st.text_input("Enter file name")

    if st.button("Generate"):

        if file_name.strip() != "":

            if option == "Audio":
                success, result = text_to_audio(st.session_state["summary"], file_name)

                if success:
                    with open(result, "rb") as f:
                        st.download_button("Download Audio", f, file_name=result)

                    st.audio(result)

            elif option == "PDF":
                
                success, result = text_to_pdf(keyword, st.session_state["summary"], file_name)

                if success:
                    with open(result, "rb") as f:
                        st.download_button("Download PDF", f, file_name=result)