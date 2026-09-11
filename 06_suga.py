import streamlit as st

st.set_page_config(
    page_title="SUGA | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# =========================
# PAGE STYLE
# =========================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top right, #7650B5 0%, transparent 35%),
        radial-gradient(circle at bottom left, #3F2168 0%, transparent 40%),
        linear-gradient(135deg, #211033, #0E0717);
    color: white;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* TITLE */

h1 {
    text-align: center !important;
    font-size: 64px !important;
    font-weight: 800 !important;
    letter-spacing: 5px !important;
    color: white !important;
    margin-top: 0 !important;
    margin-bottom: 5px !important;
}

/* SUBTITLE */

.suga-subtitle {
    text-align: center;
    font-size: 20px;
    color: #DCC8FF;
    margin-bottom: 5px;
}

/* LINE */

.suga-line {
    width: 100px;
    height: 4px;
    margin: 18px auto 35px auto;
    border-radius: 10px;
    background: linear-gradient(90deg, #BFA0FF, #7650B5);
}

/* INTRO TEXT */

.suga-intro {
    text-align: center;
    font-size: 17px;
    line-height: 1.8;
    color: #EEE4F8;
}

/* CARD */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(77, 40, 111, 0.55);
    border: 1px solid rgba(200, 175, 240, 0.22);
    border-radius: 20px;
    padding: 20px;
}

/* CARD HEADING */

.card-heading {
    font-size: 23px;
    font-weight: 700;
    color: white;
}

/* CARD TEXT */

.card-text {
    font-size: 15px;
    line-height: 1.7;
    color: #E9DDF4;
}

/* QUOTE */

.quote-text {
    text-align: center;
    color: #E7D4FF;
    font-size: 18px;
    font-style: italic;
    padding: 10px;
}

/* INFO */

div[data-testid="stAlert"] {
    background: rgba(104, 58, 145, 0.30);
    border: 1px solid rgba(200, 175, 240, 0.20);
    color: #EEE4F8;
}

/* BUTTONS */

.stButton > button {
    width: 100%;
    border-radius: 13px;
    border: 1px solid rgba(215, 190, 250, 0.40);
    background: linear-gradient(135deg, #8C62C2, #54327D);
    color: white;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #A57BD5, #6D4498);
    color: white;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.title("SUGA")

st.markdown(
    '<p class="suga-subtitle">'
    'Rapper • Producer • Songwriter • Artist'
    '</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="suga-line"></p>',
    unsafe_allow_html=True
)

# =========================
# INTRODUCTION
# =========================

st.markdown("### Min Yoongi")

st.markdown(
    """
    <p class="suga-intro">
    SUGA is one of BTS's rappers and is also known for his work
    as a songwriter and producer. His music is often recognized
    for its honesty, emotional depth and personal storytelling.
    </p>
    """,
    unsafe_allow_html=True
)

st.info(
    "SUGA's journey as an artist reflects his passion for music, "
    "his determination and his distinctive creative style."
)


# =========================
# FIRST ROW
# =========================

st.write("")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):

        st.markdown(
            '<p class="card-heading">🎤 About SUGA</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p class="card-text">
            SUGA is known for his calm personality, straightforward nature
            and strong dedication to music. His lyrics often discuss
            real experiences, emotions, dreams and personal growth.
            </p>
            """,
            unsafe_allow_html=True
        )


with col2:
    with st.container(border=True):

        st.markdown(
            '<p class="card-heading">🎵 Role in BTS</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p class="card-text">
            As a rapper, songwriter and producer, SUGA has contributed
            to the musical identity of BTS. His production and writing
            have helped shape many memorable songs.
            </p>
            """,
            unsafe_allow_html=True
        )


# =========================
# SECOND ROW
# =========================

st.write("")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):

        st.markdown(
            '<p class="card-heading">🎧 Music & Production</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p class="card-text">
            SUGA has worked extensively in songwriting and music production.
            His work is known for combining strong beats with thoughtful
            lyrics and emotional storytelling.
            </p>
            """,
            unsafe_allow_html=True
        )


with col4:
    with st.container(border=True):

        st.markdown(
            '<p class="card-heading">🖤 Agust D</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p class="card-text">
            Under the name Agust D, SUGA explores a more personal and
            introspective side of his artistry. His solo work allows him
            to express ideas and experiences in his own distinctive style.
            </p>
            """,
            unsafe_allow_html=True
        )


# =========================
# SPECIAL SECTION
# =========================

st.write("")

with st.container(border=True):

    st.markdown(
        '<p class="card-heading">💜 His Journey</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="card-text">
        SUGA's journey shows how dedication and creativity can turn
        challenges into artistic expression. From performing with BTS
        to creating music as a solo artist and producer, he has developed
        a distinctive place in the music world.
        </p>
        """,
        unsafe_allow_html=True
    )


# =========================
# QUOTE
# =========================

st.write("")

with st.container(border=True):

    st.markdown(
        '<p class="quote-text">'
        'A quiet strength, a powerful mind and a passion for music.'
        '</p>',
        unsafe_allow_html=True
    )


# =========================
# NAVIGATION
# =========================

st.write("")
st.write("")

back_col, next_col = st.columns(2)

with back_col:
    if st.button("← Back to Jin", key="back_jin"):
        st.switch_page("pages/05_jin.py")


with next_col:
    if st.button("Next: J-Hope →", key="next_jhope"):
        st.switch_page("pages/07_jhope.py")