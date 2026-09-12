import streamlit as st

st.set_page_config(
    page_title="RM | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# =========================
# CSS
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
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

.title {
    text-align: center;
    font-size: 62px;
    font-weight: 800;
    letter-spacing: 5px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #E6D5FF;
}

.line {
    width: 100px;
    height: 4px;
    margin: 18px auto 35px auto;
    border-radius: 10px;
    background: linear-gradient(90deg, #D0AEFF, #8E5BC5);
}

/* CARD */
.card {
    background: rgba(82, 43, 116, 0.58);
    border: 1px solid rgba(220, 190, 255, 0.25);
    border-radius: 22px;
    padding: 28px;
    margin-bottom: 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.22);
}

.card h2 {
    color: #DDBFFF;
    font-size: 24px;
    margin-top: 0;
    margin-bottom: 12px;
}

.card p {
    color: #F0E7F7;
    font-size: 16px;
    line-height: 1.75;
    margin: 0;
}

/* INTRO */
.intro {
    background: rgba(75, 38, 105, 0.68);
    border: 1px solid rgba(220, 190, 255, 0.25);
    border-radius: 25px;
    padding: 32px;
    margin-bottom: 30px;
    text-align: center;
    box-shadow: 0 12px 35px rgba(0,0,0,0.25);
}

.intro h2 {
    color: #DDBFFF;
    margin-bottom: 15px;
}

.intro p {
    color: #F3EBFA;
    font-size: 17px;
    line-height: 1.8;
}

/* QUOTE */
.quote {
    background: rgba(104, 58, 145, 0.35);
    border: 1px solid rgba(215, 186, 255, 0.20);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    margin: 35px auto;
}

.quote p {
    color: #E7D4FF;
    font-size: 18px;
    font-style: italic;
}

/* BUTTON */
.stButton > button {
    width: 100%;
    border-radius: 13px;
    border: 1px solid rgba(224,202,255,0.40);
    background: linear-gradient(135deg,#9C6AD0,#60358E);
    color: white;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg,#B98CE7,#7749A8);
    color: white;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================

# =========================
# HEADER
# =========================

st.markdown("""
<h1 style="
    text-align:center;
    font-size:64px;
    font-weight:800;
    letter-spacing:5px;
    color:white;
    margin:0 0 5px 0;
">
    RM
</h1>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Leader • Rapper • Songwriter • Artist</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="line"></div>',
    unsafe_allow_html=True
)


# =========================
# INTRODUCTION
# =========================

st.markdown("""
<section class="intro">
    <h2>Kim Namjoon</h2>
    <p>
        RM is the leader of BTS and one of the group's main rappers.
        He is known for his thoughtful lyrics, love for literature and art,
        and his ability to express meaningful ideas through music.
    </p>
    <p>
        As the leader, RM has played an important role in bringing
        the seven members together and representing BTS around the world.
    </p>
</section>
""", unsafe_allow_html=True)


# =========================
# INFORMATION
# =========================

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <section class="card">
        <h2>🌙 About RM</h2>
        <p>
            RM is widely admired for his intelligence, calm personality
            and thoughtful way of speaking. His lyrics often explore
            identity, growth, dreams and life experiences.
        </p>
    </section>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <section class="card">
        <h2>🎤 Role in BTS</h2>
        <p>
            As BTS's leader and rapper, RM contributes to songwriting,
            rap performances and the creative direction of the group.
            He also represents BTS at important public events.
        </p>
    </section>
    """, unsafe_allow_html=True)


col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <section class="card">
        <h2>🎵 Music</h2>
        <p>
            RM has participated in writing and producing BTS songs
            and has also released solo music. His solo work gives
            listeners another look into his thoughts and artistic style.
        </p>
    </section>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <section class="card">
        <h2>🎨 Love for Art</h2>
        <p>
            RM has a strong interest in art, museums and literature.
            He often shares his appreciation for artworks and artists,
            making art an important part of his personal world.
        </p>
    </section>
    """, unsafe_allow_html=True)


# =========================
# LEADERSHIP
# =========================

st.markdown("""
<section class="card">
    <h2>💜 His Leadership</h2>
    <p>
        RM's leadership is often reflected in the way he communicates,
        supports the members and represents BTS. His thoughtful approach
        has become an important part of the group's identity.
    </p>
</section>
""", unsafe_allow_html=True)


# =========================
# QUOTE
# =========================

st.markdown("""
<section class="quote">
    <p>
        A journey is made of many moments, and every moment becomes
        part of the story.
    </p>
</section>
""", unsafe_allow_html=True)


# =========================
# NAVIGATION
# =========================

back, next_page = st.columns(2)

with back:
    if st.button("← Back to Members"):
        st.switch_page("pages/03_Members.py")

with next_page:
    if st.button("Next: Jin →"):
        st.switch_page("pages/05_jin.py")
