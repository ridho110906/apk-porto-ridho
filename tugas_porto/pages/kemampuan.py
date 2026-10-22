import streamlit as st
import streamlit.components.v1 as components

st.title("Minat dan Kemampuan Saya")

st.page_link("home.py", label="Kembali Ke Beranda",icon="🏠")


st.markdown(
    """
    <style>
    .stApp {
        background-color: #c0c0c0;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


with open("tugas_porto/pages/tes.html", "r") as f:
    kode_html = f.read()

components.html(kode_html, height=1500, scrolling=True)


st.markdown(
    """
    <style>
    [data-testid="stPageLink"] a {
        background-color: teal;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: teal;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
