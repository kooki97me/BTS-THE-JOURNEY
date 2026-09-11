import streamlit as st

st.set_page_config(
    page_title="Jungkook | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# ==================== PURPLE THEME ====================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top right, #9A55D6 0%, transparent 35%),
        radial-gradient(circle at bottom left, #572477 0%, transparent 40%),
        linear-gradient(135deg, #32104F, #170822, #0B050F);
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

/* Headings */
h2, h3 {
    color: #FFFFFF !important;
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
    background-color: rgba(119, 62, 165, 0.35) !important;
    border: 1px solid rgba(215, 180, 250, 0.35) !important;
    color: #F3E8FF !important;
}

/* Success box */
[data-testid="stSuccess"] {
    background-color: rgba(91, 45, 130, 0.40) !important;
    border: 1px solid rgba(215, 180, 250, 0.35) !important;
    color: #F5EAFF !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid rgba(225, 195, 255, 0.45);
    background: linear-gradient(135deg, #A35BD8, #65338D);
    color: #FFFFFF;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #C080E8, #7A469F);
    border-color: #E8D5FF;
    color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)


# ==================== TITLE ====================

st.title("JUNGKOOK")

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

st.header("Jeon Jungkook")

st.write(
    "Jungkook is the youngest member of BTS, known for his vocals, "
    "dance, performances and versatility. His journey with BTS shows "
    "how continuous practice and determination can lead to remarkable growth."
)

st.info(
    "Jungkook is often called the 'Golden Maknae' because of his ability "
    "to take on many different aspects of performance and music."
)


# ==================== VOCALS & DANCE ====================

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎤 Vocals")

    st.write(
        "Jungkook's versatile vocals allow him to handle different musical "
        "styles. His voice has become an important part of BTS's sound."
    )

with col2:
    st.subheader("🕺 Dance & Performance")

    st.write(
        "Known for his strong stage presence and precise dancing, "
        "Jungkook brings energy and confidence to BTS performances."
    )


# ==================== VERSATILITY ====================

st.divider()

st.header("🌟 The Golden Maknae")

st.write(
    "Jungkook has developed skills across singing, dancing, songwriting "
    "and performance. His versatility is one of the qualities that has "
    "made him stand out throughout BTS's career."
)


# ==================== PERSONALITY ====================

st.header("✨ Personality")

st.write(
    "Jungkook is known for his hardworking nature, curiosity and playful "
    "personality. Over the years, fans have watched him grow from BTS's "
    "youngest member into a confident artist."
)


# ==================== JOURNEY ====================

st.header("💜 His Journey")

st.write(
    "Jungkook joined BTS at a young age and grew alongside the other six "
    "members. From early performances to major global stages, his journey "
    "reflects years of learning, practice and personal growth."
)


# ==================== SOLO MUSIC ====================

st.header("🎵 Solo Music")

st.write(
    "Jungkook has also explored his own musical identity through solo "
    "projects, giving listeners a chance to experience different sides "
    "of his artistry."
)

st.success(
    "Jungkook's journey represents continuous growth, versatility "
    "and dedication to his craft."
)


# ==================== FINAL MESSAGE ====================

st.divider()

st.subheader("💜 A Little Reminder")

st.write(
    "You do not have to be perfect from the beginning. "
    "Keep learning, keep practicing and let yourself grow."
)


# ==================== NAVIGATION ====================

st.divider()

col_back, col_home = st.columns(2)

with col_back:
    if st.button("← Back to V", key="back_v"):
        st.switch_page("pages/09_v.py")

with col_home:
    if st.button("Back to Members 💜", key="back_members"):
        st.switch_page("pages/03_Members.py")