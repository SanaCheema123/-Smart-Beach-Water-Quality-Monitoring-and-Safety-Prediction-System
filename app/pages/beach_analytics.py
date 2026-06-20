import sys
from pathlib import Path
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "app"))
from components.styles import load_css
from components.sidebar import sidebar_header
from components.data_loader import load_data

st.set_page_config(page_title="Beach Analytics | OceanAI", page_icon="📈", layout="wide")
load_css()
sidebar_header()

st.markdown('<div class="hero-box"><span class="hero-badge">Environmental Trends</span><h1>Beach Analytics</h1><p>Analyze coastal measurements and beach-wise water safety patterns.</p></div>', unsafe_allow_html=True)

df = load_data()
c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="content-card"><h3>Turbidity by Water Quality Status</h3>', unsafe_allow_html=True)
    fig = px.box(df, x="water_quality_status", y="turbidity")
    fig.update_layout(height=420)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="content-card"><h3>Beach-wise Risk Count</h3>', unsafe_allow_html=True)
    if "beach_name" in df.columns:
        fig = px.histogram(df, x="beach_name", color="water_quality_status", barmode="group")
        fig.update_layout(height=420)
        st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
