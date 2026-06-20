import sys
from pathlib import Path
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "app"))
from components.styles import load_css
from components.sidebar import sidebar_header
from components.data_loader import load_data

st.set_page_config(page_title="Environmental Insights | OceanAI", page_icon="🌿", layout="wide")
load_css()
sidebar_header()

st.markdown('<div class="hero-box"><span class="hero-badge">Water Quality Drivers</span><h1>Environmental Insights</h1><p>Discover relationships between temperature, turbidity, rainfall, bacteria, and beach safety.</p></div>', unsafe_allow_html=True)

df = load_data()
num = df.select_dtypes(include="number")

left, right = st.columns(2)
with left:
    st.markdown('<div class="content-card"><h3>Correlation Heatmap</h3>', unsafe_allow_html=True)
    fig = px.imshow(num.corr(), text_auto=".2f", aspect="auto")
    fig.update_layout(height=520)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="content-card"><h3>Bacteria vs Turbidity</h3>', unsafe_allow_html=True)
    if "bacteria_count" in df.columns and "turbidity" in df.columns:
        fig = px.scatter(df, x="turbidity", y="bacteria_count", color="water_quality_status")
        fig.update_layout(height=520)
        st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
