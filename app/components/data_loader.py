from pathlib import Path
import sys
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "src"))

@st.cache_data
def load_data():
    processed = ROOT / "data" / "processed" / "processed_water_quality.csv"
    if not processed.exists():
        from data_preprocessing import preprocess
        preprocess()
    return pd.read_csv(processed)

@st.cache_data
def load_model_comparison():
    path = ROOT / "outputs" / "model_comparison.csv"
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()

@st.cache_data
def load_confusion_matrix():
    path = ROOT / "outputs" / "confusion_matrix.csv"
    if path.exists():
        return pd.read_csv(path, index_col=0)
    return pd.DataFrame()
