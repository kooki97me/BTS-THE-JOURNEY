import streamlit as st

st.set_page_config(
    page_title="J-Hope | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# =========================
# PAGE BACKGROUND
# =========================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #9A67C7 0%, transparent 35%),
        radial-gradient(circle at bottom right, #4B2670 0%, transparent 40%),
        linear-gradient(135deg, #29143D, #100817);
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1 {
    color: white !important;
}

h2, h3 {
    color: #E7CFFF !important;
}

p {
    color: #EDE3F5;
    line-height: 1.7;
}

.stButton > button {
    width: 100%;
    border-radius: 13px;
    border: 1px solid rgba(225, 200, 255, 0.40);
    background: linear-gradient(135deg, #A06AD0, #63358D);
    color: white;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #BD8BE5, #7B4AA5);
    color: white;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.markdown(
    "<h1 style='text-align:center; font-size:64px; letter-spacing:5px;'>J-HOPE</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:20px; color:#E7CFFF;'>"
    "Dancer • Rapper • Performer • Artist"
    "</p>",
    unsafe_allow_html=True
)

st.divider()


# =========================
# INTRODUCTION
# =========================

st.markdown("## Jung Hoseok")

st.write(
    "J-Hope is a member of BTS known for his exceptional dancing, "
    "energetic performances and bright personality. He is also a "
    "rapper and songwriter who has developed his own artistic style."
)

st.info(
    "His stage name represents his role as a source of hope and "
    "positive energy for BTS and their fans."
)


# =========================
# FIRST ROW
# =========================

st.write("")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🕺 Dance")

    st.write(
        "J-Hope is widely recognized for his powerful dance skills "
        "and precise movements. His performances often stand out "
        "because of his energy, control and expressive style."
    )

with col2:
    st.markdown("### 🎤 Role in BTS")

    st.write(
        "As a rapper, dancer and performer, J-Hope contributes to "
        "BTS's music and stage performances. His presence adds "
        "energy and a distinctive performance style to the group."
    )


# =========================
# SECOND ROW
# =========================

st.write("")
st.divider()
st.write("")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### 🎵 Music")

    st.write(
        "J-Hope has participated in songwriting and has also explored "
        "his own musical identity through solo projects. His music "
        "often combines hip-hop influences with his personal style."
    )

with col4:
    st.markdown("### 🌟 Personality")

    st.write(
        "J-Hope is known for his cheerful and energetic personality. "
        "He often brings a positive atmosphere to the group and "
        "helps create memorable moments with the other members."
    )


# =========================
# SPECIAL SECTION
# =========================

st.write("")
st.divider()
st.write("")

st.markdown("## 💜 His Journey")

st.write(
    "J-Hope's journey is closely connected with dance, music and "
    "performance. From developing his skills as a dancer to becoming "
    "a successful member and solo artist, he has created a distinctive "
    "place for himself in BTS's story."
)

st.success(
    "J-Hope's biggest strength as a performer is the energy he brings "
    "to the stage."
)


# =========================
# QUOTE
# =========================

st.write("")
st.markdown("### ✨ The Spirit of J-Hope")

st.write(
    "Energy on stage, creativity through music and a personality "
    "that brings brightness to the journey."
)


# =========================
# NAVIGATION
# =========================

st.write("")
st.write("")

back_col, next_col = st.columns(2)

with back_col:
    if st.button("← Back to SUGA", key="back_suga"):
        st.switch_page("pages/06_suga.py")

with next_col:
    if st.button("Next: Jimin →", key="next_jimin"):
        st.switch_page("pages/08_jimin.py")
