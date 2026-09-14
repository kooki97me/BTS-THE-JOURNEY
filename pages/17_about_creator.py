import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="About the Creator | BTS: The Journey",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# PURPLE THEME
# --------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #170B27 0%,
        #281340 50%,
        #190B2B 100%
    );
    color: #F4ECFA;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

.block-container {
    max-width: 1000px;
    padding-top: 2rem;
    padding-bottom: 2.5rem;
}

/* Main title */
h1 {
    color: #F1E5FF !important;
    text-align: center;
    font-size: 38px !important;
    font-weight: 700 !important;
}

/* Section headings */
h2, h3 {
    color: #E4CFFA !important;
}

/* Paragraph */
p {
    color: #D8C9E5;
    line-height: 1.7;
}

/* Technology boxes */
.tech-box {
    background: rgba(190, 150, 230, 0.08);
    border: 1px solid rgba(205, 175, 240, 0.18);
    border-radius: 12px;
    padding: 13px 5px;
    text-align: center;
}

.tech-name {
    color: #E8D9F8;
    font-size: 15px;
    font-weight: 600;
}

.tech-desc {
    color: #BBA8C9;
    font-size: 12px;
}

/* Bottom text */
.bottom-text {
    text-align: center;
    color: #9D8CAA;
    font-size: 13px;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("ABOUT THE CREATOR")

st.markdown(
    """
    <p style="
        text-align:center;
        color:#CBB5DF;
        font-size:16px;
    ">
        The person behind BTS: The Journey 💜
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <hr style="
        width:70px;
        border:0;
        height:3px;
        background:#B58ADD;
        border-radius:10px;
        margin:15px auto 28px auto;
    ">
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# CREATOR
# --------------------------------------------------
st.markdown(
    "<h2 style='text-align:center;'>Komal Kumari</h2>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align:center;
        color:#BBA4D0;
        font-size:14px;
    ">
        Computer Science & Engineering Student
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")

st.write(
    "Hi! I'm Komal Kumari, a Computer Science & Engineering student "
    "with an interest in technology, web development, and AI. "
    "BTS: The Journey is a personal project where I combined "
    "what I enjoy learning with my interest in BTS."
)

st.write(
    "I created this website to make it easy for ARMYs, especially "
    "those who are new to BTS, to explore their members, music, "
    "achievements, stories, and journey in one place. Building this "
    "project also gave me an opportunity to learn and improve my "
    "skills in Python, Streamlit, UI design, database handling, "
    "and web application deployment."
)


# --------------------------------------------------
# ABOUT PROJECT
# --------------------------------------------------
st.markdown("### 💜 About BTS: The Journey")

st.write(
    "BTS: The Journey is an interactive fan-made web application "
    "created to bring information about BTS members, music, "
    "achievements, timeline, stories, and ARMY Space together "
    "in one place."
)


# --------------------------------------------------
# TECHNOLOGIES
# --------------------------------------------------
st.markdown("### 🛠️ Technologies Used")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("### 🐍")
    st.markdown("**Python**")
    st.caption("Programming")

with col2:
    st.markdown("### ⚡")
    st.markdown("**Streamlit**")
    st.caption("Web application")

with col3:
    st.markdown("### 🎨")
    st.markdown("**HTML / CSS**")
    st.caption("UI & styling")

with col4:
    st.markdown("### 🗄️")
    st.markdown("**SQLite**")
    st.caption("Database")

with col5:
    st.markdown("### 🖼️")
    st.markdown("**Pillow**")
    st.caption("Image processing")


# --------------------------------------------------
# COPYRIGHT
# --------------------------------------------------
st.markdown("### © Copyright & Declaration")

copyright_box = st.container(border=True)

with copyright_box:

    st.markdown(
        "#### © 2026 Komal Kumari. All Rights Reserved."
    )

    st.write(
        "BTS: The Journey is an original personal project created "
        "and developed by Komal Kumari. The original source code, "
        "written content, design, and project structure created "
        "for this website are the property of the creator and "
        "may not be copied, reproduced, modified, or redistributed "
        "without permission."
    )


# --------------------------------------------------
# FAN-MADE DECLARATION
# --------------------------------------------------
declaration_box = st.container(border=True)

with declaration_box:

    st.markdown("#### 💜 Fan-made Project Declaration")

    st.write(
        "This website is an unofficial, fan-made project created "
        "for educational and entertainment purposes. It is not "
        "affiliated with, sponsored by, or endorsed by BTS, "
        "BIGHIT MUSIC, HYBE, or Weverse. BTS-related names, "
        "trademarks, photographs, music, videos, and other "
        "third-party materials belong to their respective owners."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
    <p class="bottom-text">
        Made with 💜 for ARMY
        <br><br>
        © 2026 Komal Kumari • BTS: The Journey
    </p>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# BACK TO HOME
# --------------------------------------------------
st.write("")

if st.button("← Back to Home"):
    st.switch_page("pages/02_Home.py")
