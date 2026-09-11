import streamlit as st

st.set_page_config(
    page_title="V | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# ==================== PURPLE THEME ====================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #7046B8 0%, transparent 35%),
        radial-gradient(circle at bottom right, #43206B 0%, transparent 40%),
        linear-gradient(135deg, #29103F, #13081E, #09040D);
    color: #FFFFFF;
}

/* Main title */
h1 {
    text-align: center !important;
    color: #FFFFFF !important;
    font-size: 58px !important;
    font-weight: 800 !important;
    letter-spacing: 4px !important;
    margin-top: 25px !important;
}

/* Headings */
h2, h3 {
    color: #FFFFFF !important;
}

/* Normal text */
p {
    color: #EDE2F8 !important;
    line-height: 1.7 !important;
}

/* Divider */
hr {
    border-color: rgba(220, 190, 255, 0.25) !important;
}

/* Info box */
[data-testid="stInfo"] {
    background-color: rgba(104, 57, 145, 0.35) !important;
    border: 1px solid rgba(210, 177, 245, 0.35) !important;
    color: #F3E9FF !important;
}

/* Success box */
[data-testid="stSuccess"] {
    background-color: rgba(82, 43, 119, 0.40) !important;
    border: 1px solid rgba(210, 177, 245, 0.35) !important;
    color: #F4E9FF !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid rgba(220, 190, 255, 0.45);
    background: linear-gradient(135deg, #9258C7, #5C3285);
    color: #FFFFFF;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #B27ADC, #74449D);
    border-color: #E5D0FF;
    color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)


# ==================== TITLE ====================

st.title("V")

st.markdown(
    """
    <p style="
        text-align:center;
        color:#DCC5F5;
        font-size:20px;
        margin-top:-15px;
        margin-bottom:25px;
    ">
        Vocalist • Performer • Artist
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# ==================== INTRODUCTION ====================

st.header("Kim Taehyung")

st.write(
    "V is a member of BTS known for his distinctive voice, "
    "artistic personality and unique approach to performance. "
    "His individuality has become an important part of his identity as an artist."
)

st.info(
    "V's journey reflects creativity, individuality and the confidence "
    "to express himself in his own way."
)


# ==================== VOICE & PERFORMANCE ====================

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎤 Distinctive Voice")

    st.write(
        "V has a deep and recognizable vocal tone that gives many BTS "
        "songs a distinctive character. His voice can create both "
        "warm and powerful moments."
    )

with col2:
    st.subheader("🎭 Performance")

    st.write(
        "His expressive stage presence and unique performance style "
        "make him stand out. He often brings a strong sense of character "
        "and emotion to performances."
    )


# ==================== ART & PHOTOGRAPHY ====================

st.divider()

st.header("🎨 Love for Art")

st.write(
    "V has shown an interest in photography, visual art and different "
    "forms of creative expression. His artistic interests extend beyond "
    "music and influence the way he sees and presents the world."
)


# ==================== PERSONALITY ====================

st.header("✨ Personality")

st.write(
    "V is known for his playful, expressive and sometimes unpredictable "
    "personality. His individuality and creativity have made him a memorable "
    "part of BTS."
)


# ==================== JOURNEY ====================

st.header("💜 His Journey")

st.write(
    "From his early years with BTS to his growth as a solo artist, "
    "V has continued exploring different sides of his creativity. "
    "His journey shows how an artist can keep developing while staying true "
    "to their own identity."
)


# ==================== SOLO MUSIC ====================

st.header("🎵 Solo Music")

st.write(
    "V has explored his individual musical style through solo releases, "
    "bringing his distinctive voice and artistic personality into his own music."
)

st.success(
    "V's artistry is a combination of distinctive vocals, creativity "
    "and a strong individual identity."
)


# ==================== FINAL MESSAGE ====================

st.divider()

st.subheader("💜 A Little Reminder")

st.write(
    "Being different can be a strength. Your own way of seeing the world "
    "can become the thing that makes your journey special."
)


# ==================== NAVIGATION ====================

st.divider()

col_back, col_next = st.columns(2)

with col_back:
    if st.button("← Back to Jimin", key="back_jimin"):
        st.switch_page("pages/08_jimin.py")

with col_next:
    if st.button("Next: Jungkook →", key="next_jk"):
        st.switch_page("pages/10_jk.py")