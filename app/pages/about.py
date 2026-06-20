import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "app"))
from components.styles import load_css
from components.sidebar import sidebar_header
from components.cards import section_card

st.set_page_config(page_title="About | OceanAI", page_icon="ℹ️", layout="wide")
load_css()
sidebar_header()

st.markdown('<div class="hero-box"><span class="hero-badge">Project Overview</span><h1>About OceanAI Beach Water Quality Project</h1><p>A portfolio-ready environmental machine learning project for beach safety monitoring.</p></div>', unsafe_allow_html=True)

section_card("Project Objective", "This system predicts beach water safety status using machine learning and environmental sensor features.")
section_card("Dataset", "The project is designed for the Kaggle Beach Water Quality dataset. A sample dataset is included so the app runs immediately.")
section_card("Technology Stack", "Python, Streamlit, Pandas, NumPy, Scikit-learn, Plotly, Joblib, and XGBoost.")
section_card("Workflow", "Dataset → Cleaning → Feature Engineering → Model Training → Evaluation → Prediction Dashboard → Reports.")
