import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="CyberShield Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Security Analytics Dashboard")

df = pd.read_csv("data/history.csv")

if len(df) == 0:
    st.warning("No analysis history found.")
    st.stop()

# =====================
# Metrics
# =====================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📧 Total Emails",
        len(df)
    )

with col2:
    st.metric(
        "🎯 Avg Threat Score",
        round(df["score"].mean(), 1)
    )

with col3:
    phishing_count = (df["prediction"] == 1).sum()

    st.metric(
        "🚨 Phishing Detected",
        phishing_count
    )

st.markdown("---")

# =====================
# Charts
# =====================

df["timestamp"] = pd.to_datetime(df["timestamp"])

pie = px.pie(
    df,
    names="prediction",
    title="Email Classification Distribution"
)

line = px.line(
    df,
    x="timestamp",
    y="score",
    title="Threat Score Trend"
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        pie,
        use_container_width=True,
        key="classification_pie"
    )

with col2:
    st.plotly_chart(
        line,
        use_container_width=True,
        key="threat_trend"
    )

st.markdown("---")

# =====================
# History Table
# =====================

st.subheader("📋 Analysis History")

st.dataframe(
    df,
    use_container_width=True
)