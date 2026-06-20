import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "app"))
sys.path.append(str(ROOT / "src"))

from components.styles import load_css
from components.sidebar import sidebar_header
from predict import predict_water_quality

st.set_page_config(page_title="Prediction | OceanAI", page_icon="🔮", layout="wide")
load_css()
sidebar_header()

st.markdown(
    '''
    <div class="hero-box">
        <span class="hero-badge">AI Prediction Engine</span>
        <h1>Water Quality Safety Prediction</h1>
        <p>Enter current beach and sensor measurements to predict whether water is safe, moderate risk, or unsafe.</p>
    </div>
    ''',
    unsafe_allow_html=True
)

left, right = st.columns([1, 1])

with left:
    st.markdown('<div class="content-card"><h3>Sensor Input Panel</h3></div>', unsafe_allow_html=True)
    beach_name = st.selectbox("Beach Name", ["North Beach", "Palm Coast", "Blue Bay", "Silver Shore", "Coral Point"])
    water_temperature = st.number_input("Water Temperature (°C)", 5.0, 45.0, 24.0)
    air_temperature = st.number_input("Air Temperature (°C)", 5.0, 50.0, 28.0)
    turbidity = st.number_input("Turbidity", 0.0, 50.0, 4.5)
    wave_height = st.number_input("Wave Height (m)", 0.0, 8.0, 0.8)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 150.0, 5.0)
    ph = st.number_input("pH", 5.0, 10.0, 7.6)
    dissolved_oxygen = st.number_input("Dissolved Oxygen", 0.0, 15.0, 7.2)
    conductivity = st.number_input("Conductivity", 1000.0, 70000.0, 42000.0)
    bacteria_count = st.number_input("Bacteria Count", 0.0, 2000.0, 80.0)

    predict_btn = st.button("Predict Water Safety")

with right:
    st.markdown('<div class="content-card"><h3>Prediction Result</h3>', unsafe_allow_html=True)
    if predict_btn:
        inputs = {
            "beach_name": beach_name,
            "water_temperature": water_temperature,
            "air_temperature": air_temperature,
            "turbidity": turbidity,
            "wave_height": wave_height,
            "rainfall": rainfall,
            "ph": ph,
            "dissolved_oxygen": dissolved_oxygen,
            "conductivity": conductivity,
            "bacteria_count": bacteria_count
        }
        label, conf = predict_water_quality(inputs)
        confidence = f"{conf*100:.2f}%" if conf is not None else "N/A"

        if label == "Safe":
            st.success(f"Prediction: {label}")
            recommendation = "Safe for swimming and recreational activity."
        elif label == "Moderate Risk":
            st.warning(f"Prediction: {label}")
            recommendation = "Caution required. Monitor water condition before swimming."
        else:
            st.error(f"Prediction: {label}")
            recommendation = "Beach closure or public safety warning recommended."

        st.metric("Confidence Score", confidence)
        st.write("Recommendation:", recommendation)
    else:
        st.info("Fill the sensor panel and click Predict Water Safety.")
    st.markdown('</div>', unsafe_allow_html=True)
