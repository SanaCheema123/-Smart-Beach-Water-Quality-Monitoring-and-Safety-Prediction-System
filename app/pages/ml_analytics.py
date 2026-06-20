import sys
from pathlib import Path
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "app"))
from components.styles import load_css
from components.sidebar import sidebar_header
from components.data_loader import load_model_comparison, load_confusion_matrix

st.set_page_config(page_title="ML Analytics | OceanAI", page_icon="🤖", layout="wide")
load_css()
sidebar_header()

st.markdown('<div class="hero-box"><span class="hero-badge">Model Evaluation</span><h1>Machine Learning Analytics</h1><p>Review model performance, comparison results, and classification quality.</p></div>', unsafe_allow_html=True)

comp = load_model_comparison()
if comp.empty:
    st.warning("Model comparison not found. Run: py src\\train_model.py")
else:
    st.markdown('<div class="content-card"><h3>Model Comparison</h3>', unsafe_allow_html=True)
    st.dataframe(comp, use_container_width=True, hide_index=True)
    fig = px.bar(comp, x="Model", y=["Accuracy", "Precision", "Recall", "F1 Score"], barmode="group")
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

cm = load_confusion_matrix()
if not cm.empty:
    st.markdown('<div class="content-card"><h3>Confusion Matrix</h3>', unsafe_allow_html=True)
    fig = px.imshow(cm, text_auto=True, aspect="auto")
    fig.update_layout(height=430)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
