import streamlit as st

st.set_page_config(
    page_title="BTS: The Journey",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== WELCOME PAGE THEME ====================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #8B5BC7 0%, transparent 35%),
        radial-gradient(circle at bottom right, #4B2372 0%, transparent 40%),
        linear-gradient(135deg, #2A1045, #13081F, #08040D);
    color: #FFFFFF;
}

/* Hide default sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* Main content */
.block-container {
    padding-top: 8rem;
    padding-bottom: 5rem;
}

/* Small heading */
.welcome-small {
    text-align: center;
    color: #D8B8F5;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 4px;
    margin-bottom: 12px;
}

/* Main title */
.welcome-title {
    text-align: center;
    color: #FFFFFF;
    font-size: 64px;
    font-weight: 800;
    letter-spacing: 4px;
    margin-bottom: 8px;
}

/* Purple line */
.purple-line {
    width: 120px;
    height: 4px;
    background: linear-gradient(90deg, #C89BFF, #8750C4);
    border-radius: 10px;
    margin: 20px auto 30px auto;
}

/* Subtitle */
.welcome-subtitle {
    text-align: center;
    color: #E5D4F7;
    font-size: 21px;
    line-height: 1.7;
    max-width: 750px;
    margin: auto;
}

/* Quote */
.welcome-quote {
    text-align: center;
    color: #D5B7F2;
    font-size: 17px;
    font-style: italic;
    margin-top: 35px;
}

/* Button */
.stButton {
    display: flex;
    justify-content: center;
    margin-top: 35px;
}

.stButton > button {
    width: 260px;
    border-radius: 16px;
    border: 1px solid rgba(220, 190, 255, 0.5);
    background: linear-gradient(135deg, #B27BE5, #7040A0);
    color: #FFFFFF;
    font-size: 17px;
    font-weight: 700;
    padding: 13px 25px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #C795F0, #8350B5);
    border-color: #E7D3FF;
    color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)


# ==================== WELCOME CONTENT ====================

st.markdown(
    '<div class="welcome-small">WELCOME TO</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="welcome-title">BTS: THE JOURNEY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="purple-line"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="welcome-subtitle">
        Seven members. One extraordinary journey.
        <br>
        Discover their music, stories, achievements and memories.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="welcome-quote">'
    'From seven dreams to one unforgettable journey. 💜'
    '</div>',
    unsafe_allow_html=True
)


# ==================== ENTER BUTTON ====================

if st.button("💜 Enter the Journey", key="enter_journey"):
    st.switch_page("02_Home.py")
