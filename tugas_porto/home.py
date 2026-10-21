import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="🗒️",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(100deg, #000000, #00008b, #808080);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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


col1, col2 = st.columns([2,2],)
with col1:
    st.title("Welcome Ridho Portfolio!")
    st.page_link("pages/profile.py", label="Lihat Profile", icon="👤")
    st.page_link("pages/kemampuan.py", label="Lihat Kemampuan", icon="📊")
    st.page_link("pages/sosmed.py", label="Lihat Sosmed", icon="🌐")

with col2:
    st.video("tugas_porto/pages/video.mp4",width=400,autoplay=True,loop=True,muted=False)
