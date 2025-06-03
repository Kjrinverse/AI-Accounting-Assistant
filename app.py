import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI

st.set_page_config(page_title="AI Accounting Assistant", layout="wide")
st.sidebar.title("Navigation")
menu_option = st.sidebar.radio("Go to", ["Upload", "Insights & Anomalies", "Chat", "📊 Dashboard", "🆚 Compare Files", "📘 GL Classifier", "✅ Audit Checklist"])

st.title("AI Accounting Assistant")

# ... (the full verified version of app.py pasted from canvas)
