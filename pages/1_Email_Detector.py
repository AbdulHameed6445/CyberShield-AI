import streamlit as st
import joblib
import pandas as pd
from datetime import datetime
import re
from utils.email_parser import extract_text_from_txt
from utils.explain import detect_keywords
from utils.security_analyst import generate_analysis
#from utils.bert_detector import detect_phishing

model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.title("📧 Phishing Email Detector")

uploaded_file = st.file_uploader(
    "Upload Email File",
    type=["txt"]
)

email_text = ""

if uploaded_file:
    email_text = extract_text_from_txt(uploaded_file)

    st.success("Email file loaded successfully!")

    with st.expander("View Email Content"):
        st.write(email_text)

email_text_manual = st.text_area(
    "Or Paste Email Content",
    height=250
)

if email_text_manual.strip():
    email_text = email_text_manual

if st.button("Analyze Email"):

    if email_text.strip():

        # URL Detection
        st.subheader("🌐 URLs Detected")

        urls = re.findall(r'https?://[^\s]+', email_text)

        if urls:
            for url in urls:
                st.write(url)
        else:
            st.success("No URLs detected.")

        # Prediction
        features = vectorizer.transform([email_text])

        prediction = model.predict(features)[0]

        if prediction == 1:
            st.error("🚨 PHISHING DETECTED")
        else:
            st.success("✅ LEGITIMATE EMAIL")

        # Keyword Detection
        keywords = detect_keywords(email_text)

                        # Threat Score
        score = min(len(keywords) * 15, 100)

        st.subheader("🎯 Threat Score")

        st.progress(score / 100)

        st.metric("Risk Score", f"{score}%")

        analysis = generate_analysis(
            prediction,
            score,
            keywords,
            urls
        )

        st.subheader("🔍 Suspicious Indicators")

        if keywords:
            st.warning(", ".join(keywords))
        else:
            st.success("No suspicious keywords detected.")

        # Save History
        new_record = pd.DataFrame({
            "timestamp": [datetime.now()],
            "prediction": [prediction],
            "score": [score]
        })

        history = pd.read_csv("data/history.csv")

        history = pd.concat(
            [history, new_record],
            ignore_index=True
        )

        history.to_csv(
            "data/history.csv",
            index=False
        )

        st.subheader("🤖 AI Security Analyst")

        st.info(f"Threat Level: {analysis['threat_level']}")

        st.write("### Reasons")

        for reason in analysis["reasons"]:
            st.write("•", reason)

        st.write("### Recommendation")

        st.success(analysis["recommendation"])

        # Incident Report
        st.subheader("📄 Security Incident Report")

        report = f"""
Incident Type: {'Phishing' if prediction == 1 else 'Legitimate'}

Threat Score: {score}%

Risk Level:
{'Critical' if score >= 80 else 'High' if score >= 50 else 'Medium' if score >= 20 else 'Low'}

Suspicious Keywords:
{', '.join(keywords) if keywords else 'None'}

URLs Found:
{len(urls)}

Recommended Action:
{'Do not click links. Report sender and block email.'
if prediction == 1
else 'Email appears safe.'}
"""

        st.text_area(
            "Generated Report",
            report,
            height=250
        )

        st.download_button(
            label="⬇ Download Incident Report",
            data=report,
            file_name="incident_report.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please enter email content.")