import streamlit as st

st.set_page_config(
    page_title="Jin | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# =========================
# BACKGROUND & STYLE
# =========================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top right, #8E63C7 0%, transparent 35%),
        radial-gradient(circle at bottom left, #542B7D 0%, transparent 40%),
        linear-gradient(135deg, #2A1740, #12091D);
    color: white;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* JIN TITLE */

h1 {
    text-align: center !important;
    color: white !important;
    font-size: 64px !important;
    font-weight: 800 !important;
    letter-spacing: 6px !important;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

/* SUBTITLE */

.jin-subtitle {
    text-align: center;
    color: #E6D5FF;
    font-size: 20px;
    margin-top: 5px;
    margin-bottom: 5px;
}

/* STAR */

.jin-star {
    text-align: center;
    color: #C9A8EA;
    font-size: 25px;
    margin-top: 0;
    margin-bottom: 30px;
}

/* TEXT */

.jin-name {
    text-align: center;
    color: #DDBFFF;
    font-size: 27px;
    font-weight: 700;
}

.jin-heading {
    color: #DDBFFF;
    font-size: 24px;
    font-weight: 700;
}

.jin-text {
    color: #E9DDF3;
    font-size: 15px;
    line-height: 1.7;
}

.jin-intro {
    text-align: center;
    color: #F3EBFA;
    font-size: 17px;
    line-height: 1.8;
}

.jin-quote {
    text-align: center;
    color: #E7D4FF;
    font-size: 18px;
    font-style: italic;
    line-height: 1.7;
}

/* CARDS */

[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(82, 43, 116, 0.58);
    border: 1px solid rgba(220, 190, 255, 0.25);
    border-radius: 22px;
    padding: 22px;
    margin-bottom: 20px;
}

/* BUTTONS */

.stButton > button {
    width: 100%;
    border-radius: 13px;
    border: 1px solid rgba(224, 202, 255, 0.40);
    background: linear-gradient(135deg, #9C6AD0, #60358E);
    color: white;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #B98CE7, #7749A8);
    color: white;
}

</style>
""", unsafe_allow_html=True)


# =========================
# JIN — FIRST THING ON PAGE
# =========================

st.title("JIN")

st.markdown(
    '<p class="jin-subtitle">Vocalist • Visual • Worldwide Handsome</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="jin-star">✦</p>',
    unsafe_allow_html=True
)


# =========================
# INTRODUCTION
# =========================

with st.container(border=True):

    st.markdown(
        '<p class="jin-name">Kim Seokjin</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="jin-intro">
        Jin is the eldest member of BTS and is known for his warm personality,
        powerful vocals and bright sense of humor. He has a unique ability
        to bring fun and positive energy to the group.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="jin-intro">
        Along with his musical talent, Jin is loved for his caring nature,
        confidence and memorable personality both on and off stage.
        </p>
        """,
        unsafe_allow_html=True
    )


# =========================
# ROW 1
# =========================

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.markdown(
            '<p class="jin-heading">🌙 About Jin</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p class="jin-text">
            Jin is the eldest member of BTS. He is known for his cheerful
            personality, kindness and ability to make the people around him
            laugh. His positive attitude has become one of his most loved
            qualities.
            </p>
            """,
            unsafe_allow_html=True
        )


with col2:

    with st.container(border=True):

        st.markdown(
            '<p class="jin-heading">🎤 Role in BTS</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p class="jin-text">
            Jin is one of BTS's vocalists. His clear and emotional voice
            adds a distinctive quality to the group's music. He also brings
            a fun and energetic presence to BTS performances.
            </p>
            """,
            unsafe_allow_html=True
        )


# =========================
# ROW 2
# =========================

col3, col4 = st.columns(2)

with col3:

    with st.container(border=True):

        st.markdown(
            '<p class="jin-heading">🎵 Music</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p class="jin-text">
            Jin has contributed many memorable vocal performances to BTS
            songs and has also released solo music. His solo work allows
            him to express his own emotions and musical style.
            </p>
            """,
            unsafe_allow_html=True
        )


with col4:

    with st.container(border=True):

        st.markdown(
            '<p class="jin-heading">🍜 Love for Food</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p class="jin-text">
            Jin has often shared his love for food and cooking. His interest
            in food became a memorable part of BTS content and helped fans
            see his playful and caring side.
            </p>
            """,
            unsafe_allow_html=True
        )


# =========================
# PERSONALITY
# =========================

with st.container(border=True):

    st.markdown(
        '<p class="jin-heading">💜 His Personality</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="jin-text">
        Jin is known for his humor, confidence and caring nature. He often
        uses jokes and playful moments to make the atmosphere lighter.
        At the same time, he has shown strong dedication to his members
        and his work as an artist.
        </p>
        """,
        unsafe_allow_html=True
    )


# =========================
# QUOTE
# =========================

with st.container(border=True):

    st.markdown(
        """
        <p class="jin-quote">
        His bright energy has always been one of the special colors
        of BTS's journey. 💜
        </p>
        """,
        unsafe_allow_html=True
    )


# =========================
# NAVIGATION
# =========================

back_col, next_col = st.columns(2)

with back_col:

    if st.button("← Back to Members", key="back_jin"):
        st.switch_page("pages/03_Members.py")

with next_col:

    if st.button("Next: SUGA →", key="next_suga"):
        st.switch_page("pages/06_suga.py")