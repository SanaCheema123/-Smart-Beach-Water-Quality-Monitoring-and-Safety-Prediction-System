import sys
from pathlib import Path
import streamlit as st
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "app"))
from components.styles import load_css
from components.sidebar import sidebar_header
from components.data_loader import load_data, load_model_comparison

st.set_page_config(page_title="Reports | OceanAI", page_icon="📄", layout="wide")
load_css()
sidebar_header()

st.markdown('<div class="hero-box"><span class="hero-badge">Export Center</span><h1>Water Quality Reports</h1><p>Download processed data, model summary, and environmental safety report.</p></div>', unsafe_allow_html=True)

df = load_data()
comp = load_model_comparison()

summary = pd.DataFrame({
    "Metric": ["Total Records", "Safe Records", "Moderate Risk Records", "Unsafe Records"],
    "Value": [
        len(df),
        int((df["water_quality_status"] == "Safe").sum()),
        int((df["water_quality_status"] == "Moderate Risk").sum()),
        int((df["water_quality_status"] == "Unsafe").sum()),
    ]
})

c1, c2, c3 = st.columns(3)
with c1:
    st.download_button("Download Processed Dataset", df.to_csv(index=False), "processed_water_quality.csv", "text/csv")
with c2:
    st.download_button("Download Safety Summary", summary.to_csv(index=False), "water_quality_summary.csv", "text/csv")
with c3:
    if not comp.empty:
        st.download_button("Download Model Report", comp.to_csv(index=False), "model_comparison.csv", "text/csv")
    else:
        st.info("Train model to generate model report.")

st.markdown('<div class="content-card"><h3>Safety Summary</h3></div>', unsafe_allow_html=True)
st.dataframe(summary, use_container_width=True, hide_index=True)
