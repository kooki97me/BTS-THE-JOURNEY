import streamlit as st

st.set_page_config(
    page_title="BTS Members | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# ==================== PURPLE THEME ====================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #7B4BC4 0%, transparent 35%),
        radial-gradient(circle at bottom right, #4A227A 0%, transparent 40%),
        linear-gradient(135deg, #24103D, #12081F);
    color: white;
}

.members-title {
    text-align: center;
    font-size: 58px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 5px;
    color: #FFFFFF;
    letter-spacing: 2px;
}

.members-subtitle {
    text-align: center;
    font-size: 19px;
    color: #E8D8FF;
    margin-bottom: 10px;
}

.purple-line {
    width: 110px;
    height: 4px;
    background: linear-gradient(90deg, #C59AFF, #8E5BD9);
    border-radius: 10px;
    margin: 20px auto 35px auto;
}

.intro {
    max-width: 850px;
    margin: auto;
    text-align: center;
    font-size: 18px;
    line-height: 1.7;
    color: #E6D9F7;
    margin-bottom: 45px;
}

.member-card {
    background: linear-gradient(
        145deg,
        rgba(125, 75, 183, 0.55),
        rgba(47, 20, 73, 0.80)
    );
    border: 1px solid rgba(210, 180, 255, 0.25);
    border-radius: 22px;
    padding: 28px 22px;
    margin-bottom: 18px;
    min-height: 245px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.30);
}

.member-name {
    font-size: 29px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 5px;
}

.member-role {
    font-size: 16px;
    color: #D8BFFF;
    font-weight: 600;
    margin-bottom: 14px;
}

.member-description {
    font-size: 15px;
    line-height: 1.6;
    color: #EEE5F8;
    margin-bottom: 15px;
}

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid rgba(220, 195, 255, 0.45);
    background: linear-gradient(135deg, #9D69D5, #63369A);
    color: white;
    font-size: 15px;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #B98BE8, #7A48B3);
    border-color: #E0C9FF;
    color: white;
}

.member-quote {
    text-align: center;
    margin-top: 35px;
    padding: 25px;
    border-radius: 18px;
    background: rgba(87, 43, 126, 0.35);
    color: #E4D2FF;
    font-size: 18px;
    font-style: italic;
}

</style>
""", unsafe_allow_html=True)


# ==================== PAGE TITLE ====================

st.markdown(
    '<div class="members-title">MEET THE MEMBERS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="members-subtitle">'
    'Seven different personalities. One unforgettable team.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="purple-line"></div>',
    unsafe_allow_html=True
)


# ==================== INTRODUCTION ====================

st.markdown("""
<div class="intro">
BTS is made up of seven members, each with their own personality,
talent and story. Together, they created a journey that reached
millions of people around the world.
<br><br>
Explore each member and discover their individual journey.
</div>
""", unsafe_allow_html=True)


# ==================== RM & JIN ====================

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="member-card">
        <div class="member-name">RM</div>
        <div class="member-role">Leader • Rapper • Songwriter</div>
        <div class="member-description">
            The leader of BTS, known for his thoughtful words,
            powerful rap and love for art, books and music.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Explore RM →", key="rm_button"):
        st.switch_page("pages/04_rm.py")


with col2:

    st.markdown("""
    <div class="member-card">
        <div class="member-name">Jin</div>
        <div class="member-role">Vocalist • Visual • Worldwide Handsome</div>
        <div class="member-description">
            Known for his beautiful vocals, bright personality,
            humor and the ability to make people smile.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Explore Jin →", key="jin_button"):
        st.switch_page("pages/05_jin.py")


# ==================== SUGA & J-HOPE ====================

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
    <div class="member-card">
        <div class="member-name">SUGA</div>
        <div class="member-role">Rapper • Producer • Songwriter</div>
        <div class="member-description">
            A talented rapper and producer known for his honest
            lyrics, powerful production and calm personality.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Explore SUGA →", key="suga_button"):
        st.switch_page("pages/06_suga.py")


with col4:

    st.markdown("""
    <div class="member-card">
        <div class="member-name">J-Hope</div>
        <div class="member-role">Dancer • Rapper • Performer</div>
        <div class="member-description">
            Known for his incredible dance skills, energetic
            performances and positive personality.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Explore J-Hope →", key="jhope_button"):
        st.switch_page("pages/07_jhope.py")


# ==================== JIMIN & V ====================

col5, col6 = st.columns(2)

with col5:

    st.markdown("""
    <div class="member-card">
        <div class="member-name">Jimin</div>
        <div class="member-role">Vocalist • Dancer • Performer</div>
        <div class="member-description">
            Recognized for his expressive dancing, unique vocals
            and emotional connection with music.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Explore Jimin →", key="jimin_button"):
        st.switch_page("pages/08_jimin.py")


with col6:

    st.markdown("""
    <div class="member-card">
        <div class="member-name">V</div>
        <div class="member-role">Vocalist • Performer • Artist</div>
        <div class="member-description">
            Known for his distinctive voice, artistic personality,
            unique style and love for photography and art.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Explore V →", key="v_button"):
        st.switch_page("pages/09_v.py")


# ==================== JUNGKOOK & OT7 ====================

col7, col8 = st.columns(2)

with col7:

    st.markdown("""
    <div class="member-card">
        <div class="member-name">Jungkook</div>
        <div class="member-role">Vocalist • Dancer • Performer</div>
        <div class="member-description">
            The youngest member of BTS, known for his vocals,
            dancing, performances and versatility.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Explore Jungkook →", key="jk_button"):
        st.switch_page("pages/10_jk.py")


with col8:

    st.markdown("""
    <div class="member-card">
        <div class="member-name">💜 OT7</div>
        <div class="member-role">Seven Members • One Journey</div>
        <div class="member-description">
            Seven individual stories come together to create
            the story of BTS.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Explore OT7 Journey →", key="ot7_button"):
        st.switch_page("pages/11_OT7.py")


# ==================== FINAL QUOTE ====================

st.markdown("""
<div class="member-quote">
    "Seven members, countless memories, one extraordinary journey."
</div>
""", unsafe_allow_html=True)