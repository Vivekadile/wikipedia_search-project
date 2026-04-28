import streamlit as st
from utils.wiki import get_summary
from utils.converter import text_to_audio, text_to_pdf


# ---------------- LOGIN ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():

    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid Credentials")


if not st.session_state.logged_in:
    login()
    st.stop()


# ---------------- MAIN APP ---------------- #

st.sidebar.success("Logged In")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()


st.title("📚 Wikipedia Assistant")

keyword = st.text_input("Enter Topic")

if st.button("Search"):

    summary, error = get_summary(keyword)

    if not error:
        st.session_state["summary"] = summary

    else:
        st.error(error)


if "summary" in st.session_state:

    st.write(st.session_state["summary"])

    option = st.radio(
        "Choose Format",
        ["Audio", "PDF"]
    )

    file_name = st.text_input("Enter File Name")

    if st.button("Generate"):

        if file_name.strip() != "":

            if option == "Audio":

                success, result = text_to_audio(
                    st.session_state["summary"],
                    file_name
                )

                if success:
                    with open(result, "rb") as f:
                        st.download_button(
                            "Download Audio",
                            f,
                            file_name=result
                        )

                    st.audio(result)

            elif option == "PDF":

                success, result = text_to_pdf(
                    keyword,
                    st.session_state["summary"],
                    file_name
                )

                if success:
                    with open(result, "rb") as f:
                        st.download_button(
                            "Download PDF",
                            f,
                            file_name=result
                        )