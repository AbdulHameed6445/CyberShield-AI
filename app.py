import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="CyberShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stMetric {
    background-color: #1A1F2E;
    padding: 15px;
    border-radius: 12px;
}

div[data-testid="stMetric"] {
    border: 1px solid #2A324B;
    padding: 10px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.image(
    "assets/logo.png",
    width=150
)

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2092/2092663.png",
        width=100
    )

    st.title("CyberShield AI")

    st.markdown("---")

    st.info(
        "AI-Powered Email Threat Detection"
    )

st.markdown("""
# 🛡️ CyberShield AI

### Intelligent Phishing Detection & Threat Analytics Platform

Detect phishing emails, analyze threats, and generate security reports using Artificial Intelligence.
""")

st.info(
    "Detect phishing emails using Machine Learning and NLP."
)