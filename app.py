import streamlit as st

st.set_page_config(
    page_title="BTS: The Journey",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.switch_page("pages/01_welcome.py")