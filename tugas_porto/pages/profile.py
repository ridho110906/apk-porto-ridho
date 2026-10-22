import streamlit as st


st.title("Profile Saya")

st.page_link("home.py", label="Kembali Ke Beranda",icon="🏠")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(90deg, #000000, #800080, #808080);
        color: white
    }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3,gap="small")
with col1:
    st.header("Hallo, Perkenalkan Nama Saya Muhammad Ridho.")
    st.write("Saya seorang mahasiswa di Universitas Nurdin Hamzah Jambi, " \
    "fakultas Ilmu Komputer, prodi Sistem Informasi.")
    st.image("tugas_porto/pages/unh1.png", width=200)

with col2:
    st.write("##")
    st.image("tugas_porto/pages/foto1.png", width=300)
    st.subheader("Hidup itu seperti naik sepeda, agar tidak jatuh kita harus terus maju, meskipun rantainya sering lepas.")

with col3:
    st.write("##")
    st.write("Hobi saya adalah olahraga, terutama bersepeda." \
    " Saya juga suka bermain game dan menonton film di waktu luang saya. " \
    "Selain itu, saya juga suka nongkrong sambil ngopi hehe...")
    st.image("tugas_porto/pages/fotohobi.jpeg", width=300)



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
