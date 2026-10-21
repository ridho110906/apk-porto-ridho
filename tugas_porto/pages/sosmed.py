import streamlit as st

st.title("Sosial Media Saya")

st.page_link("home.py", label="Kembali Ke Beranda",icon="🏠")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://acemovi.tuneskit.com/images/resource/social-media-platform.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <style>
    [data-testid="stExpander"] details summary {
        background-color: #35aaf3;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1,2])
with col1:
    with st.expander("Instagram"):
        st.write("Follow me on Instagram: [@_rdh.0](https://www.instagram.com/_rdh.0/)")
        st.image("pages/ig.png", width=50)

    with st.expander("TikTok"):
        st.write("Follow me on TikTok: [@rdh08](https://www.tiktok.com/@rdh08)")
        st.image("pages/tiktok.jpg", width=50)
    st.audio("pages/musik.mp3",autoplay=True,loop=True,width=20)
with col2:
    st.write("#")

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

