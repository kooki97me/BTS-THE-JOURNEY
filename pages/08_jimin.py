import streamlit as st

st.set_page_config(
    page_title="Jimin | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# ==================== PURPLE THEME ====================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top right, #8A4FC7 0%, transparent 35%),
        radial-gradient(circle at bottom left, #542477 0%, transparent 40%),
        linear-gradient(135deg, #30104F, #160822, #0C0612);
    color: #FFFFFF;
}

/* Main title */
h1 {
    text-align: center !important;
    color: #FFFFFF !important;
    font-size: 58px !important;
    font-weight: 800 !important;
    letter-spacing: 3px !important;
    margin-top: 25px !important;
}

/* All headings */
h2, h3 {
    color: #FFFFFF !important;
}

/* Subtitle */
.stApp [data-testid="stHeading"] + div p {
    color: #DCC5F5 !important;
}

/* Normal text */
p {
    color: #EDE1FA !important;
    line-height: 1.7 !important;
}

/* Divider */
hr {
    border-color: rgba(220, 190, 255, 0.25) !important;
}

/* Info box */
[data-testid="stInfo"] {
    background-color: rgba(116, 63, 158, 0.35) !important;
    border: 1px solid rgba(211, 176, 246, 0.35) !important;
    color: #F3E8FF !important;
}

/* Success box */
[data-testid="stSuccess"] {
    background-color: rgba(101, 52, 140, 0.40) !important;
    border: 1px solid rgba(215, 183, 247, 0.35) !important;
    color: #F4E9FF !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid rgba(220, 190, 255, 0.45);
    background: linear-gradient(135deg, #A05BD5, #65328E);
    color: #FFFFFF;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #BC82E8, #7D46A8);
    border-color: #E8D4FF;
    color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)


# ==================== TITLE ====================

st.title("JIMIN")

st.markdown(
    """
    <p style="
        text-align:center;
        color:#DCC5F5;
        font-size:20px;
        margin-top:-15px;
        margin-bottom:25px;
    ">
        Vocalist • Dancer • Performer • Artist
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# ==================== INTRODUCTION ====================

st.header("Park Jimin")

st.write(
    "Jimin is a member of BTS known for his expressive dancing, "
    "distinctive vocals and emotional connection with music. "
    "His performances often combine elegance, precision and emotion."
)

st.info(
    "Jimin's journey with BTS shows how dedication, hard work and "
    "passion can turn challenges into growth."
)


# ==================== DANCE & VOCALS ====================

col1, col2 = st.columns(2)

with col1:
    st.subheader("💃 Dance")

    st.write(
        "Jimin is widely recognized for his expressive and graceful "
        "dance style. His movements bring strong emotion and personality "
        "to BTS performances."
    )

with col2:
    st.subheader("🎤 Vocals")

    st.write(
        "His distinctive voice adds a unique color to BTS songs. "
        "He is especially known for delivering emotional and memorable "
        "vocal performances."
    )


# ==================== PERSONALITY ====================

st.divider()

st.header("✨ Personality")

st.write(
    "Jimin is often appreciated for his caring nature, warm personality "
    "and strong bond with the other members. Behind his confident stage "
    "presence, he is also known for being thoughtful and hardworking."
)


# ==================== JOURNEY ====================

st.header("💜 His Journey")

st.write(
    "From training days to becoming an internationally recognized artist, "
    "Jimin's journey has been shaped by continuous practice and dedication. "
    "His growth as a performer can be seen throughout BTS's career."
)


# ==================== SOLO MUSIC ====================

st.header("🎵 Solo Music")

st.write(
    "Jimin has also explored his individual musical identity through "
    "solo projects, allowing listeners to experience a different side "
    "of his artistry."
)

st.success(
    "Jimin's artistry combines dance, vocals and emotion into one "
    "distinctive performance style."
)


# ==================== FINAL MESSAGE ====================

st.divider()

st.subheader("💜 A Little Reminder")

st.write(
    "Growth is not always about becoming someone different. "
    "Sometimes it is about discovering how much you can improve "
    "by continuing to believe in yourself."
)


# ==================== NAVIGATION ====================

st.divider()

col_back, col_next = st.columns(2)

with col_back:
    if st.button("← Back to SUGA", key="back_suga"):
        st.switch_page("pages/06_suga.py")

with col_next:
    if st.button("Next: V →", key="next_v"):
        st.switch_page("pages/09_v.py")
