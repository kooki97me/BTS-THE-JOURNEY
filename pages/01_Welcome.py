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

/* Main background */
.stApp {
    background:
        linear-gradient(
            rgba(35, 15, 65, 0.40),
            rgba(20, 8, 40, 0.45)
        ),
        url("https://raw.githubusercontent.com/kooki97me/BTS-THE-JOURNEY/main/images/bts_group.jpg");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;

    color: #FFFFFF;
}

/* Soft purple glow over background */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background:
        radial-gradient(
            circle at center,
            rgba(170, 110, 230, 0.12),
            transparent 60%
        );
    pointer-events: none;
    z-index: 0;
}

/* Hide default sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* Main content */
.block-container {
    padding-top: 8rem;
    padding-bottom: 5rem;
    position: relative;
    z-index: 1;
}

/* Small heading */
.welcome-small {
    text-align: center;
    color: #E3C9FF;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 5px;
    margin-bottom: 12px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
}

/* Main title */
.welcome-title {
    text-align: center;
    color: #FFFFFF;
    font-size: 64px;
    font-weight: 800;
    letter-spacing: 4px;
    margin-bottom: 8px;
    text-shadow:
        0 3px 15px rgba(0,0,0,0.7),
        0 0 25px rgba(190,130,255,0.4);
}

/* Purple line */
.purple-line {
    width: 120px;
    height: 4px;
    background: linear-gradient(90deg, #D1A5FF, #8B50C7);
    border-radius: 10px;
    margin: 20px auto 30px auto;
    box-shadow: 0 0 15px rgba(190,130,255,0.7);
}

/* Subtitle */
.welcome-subtitle {
    text-align: center;
    color: #F4E9FF;
    font-size: 21px;
    line-height: 1.7;
    max-width: 750px;
    margin: auto;
    text-shadow: 0 2px 10px rgba(0,0,0,0.65);
}

/* Quote */
.welcome-quote {
    text-align: center;
    color: #E6CFFF;
    font-size: 17px;
    font-style: italic;
    margin-top: 35px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.7);
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
    border: 1px solid rgba(230, 205, 255, 0.7);
    background: linear-gradient(
        135deg,
        rgba(178, 123, 229, 0.95),
        rgba(112, 64, 160, 0.95)
    );
    color: #FFFFFF;
    font-size: 17px;
    font-weight: 700;
    padding: 13px 25px;
    box-shadow: 0 8px 25px rgba(40, 10, 70, 0.5);
}

.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #C795F0,
        #8350B5
    );
    border-color: #F0DFFF;
    color: #FFFFFF;
    box-shadow: 0 0 25px rgba(210, 160, 255, 0.6);
}

/* Mobile adjustment */
@media (max-width: 768px) {

    .block-container {
        padding-top: 5rem;
    }

    .welcome-title {
        font-size: 42px;
    }

    .welcome-small {
        font-size: 14px;
        letter-spacing: 3px;
    }

    .welcome-subtitle {
        font-size: 17px;
        padding: 0 20px;
    }

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
    st.switch_page("pages/02_Home.py")
