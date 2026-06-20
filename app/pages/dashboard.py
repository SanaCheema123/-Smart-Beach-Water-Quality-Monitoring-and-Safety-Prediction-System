import sys
from pathlib import Path
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "app"))
from components.styles import load_css
from components.sidebar import sidebar_header
from components.cards import metric_card
from components.data_loader import load_data, load_model_comparison

st.set_page_config(page_title="Dashboard | OceanAI", page_icon="🌊", layout="wide")
load_css()
sidebar_header()

st.markdown(
    '''
    <div class="hero-box">
        <span class="hero-badge">Live Coastal Water Intelligence</span>
        <h1>Beach Water Quality Dashboard</h1>
        <p>Monitor beach safety levels, water quality status, pollution indicators, and environmental risk patterns.</p>
    </div>
    ''',
    unsafe_allow_html=True
)

df = load_data()
counts = df["water_quality_status"].value_counts() if "water_quality_status" in df.columns else {}

comp = load_model_comparison()
acc = f"{comp['Accuracy'].max()*100:.2f}%" if not comp.empty and "Accuracy" in comp.columns else "Train Model"

c1, c2, c3, c4, c5 = st.columns(5)
with c1: metric_card("Total Records", len(df), "📊")
with c2: metric_card("Safe Days", int(counts.get("Safe", 0)), "✅")
with c3: metric_card("Moderate Risk", int(counts.get("Moderate Risk", 0)), "⚠️")
with c4: metric_card("Unsafe Days", int(counts.get("Unsafe", 0)), "🚫")
with c5: metric_card("Best Accuracy", acc, "🎯")

st.markdown("<br>", unsafe_allow_html=True)
left, right = st.columns([1.15, 1])

with left:
    st.markdown('<div class="content-card"><h3>Water Quality Status Distribution</h3>', unsafe_allow_html=True)
    chart_df = df["water_quality_status"].value_counts().reset_index()
    chart_df.columns = ["Status", "Records"]
    fig = px.pie(chart_df, names="Status", values="Records", hole=0.45)
    fig.update_layout(height=430, margin=dict(l=20,r=20,t=20,b=20))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="content-card"><h3>Dataset Preview</h3></div>', unsafe_allow_html=True)
    st.dataframe(df.head(12), use_container_width=True, hide_index=True)
