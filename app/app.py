import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "app"))

from components.styles import load_css
from components.sidebar import sidebar_header

st.set_page_config(
    page_title="OceanAI Beach Water Quality",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
sidebar_header()

st.markdown(
    '''
    <div class="hero-box">
        <span class="hero-badge">AI + Environmental Analytics + Beach Safety</span>
        <h1>OceanAI Coastal Intelligence Center</h1>
        <p>Professional machine learning dashboard for beach water quality monitoring, safety prediction, and environmental decision support.</p>
    </div>
    ''',
    unsafe_allow_html=True
)

st.markdown("### Welcome")
st.write("Use the sidebar pages to open Dashboard, Prediction, Analytics, Reports, and ML results.")
st.info("First run: `py src\\train_model.py` then `py -m streamlit run app\\app.py`.")
