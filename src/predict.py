from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "best_water_quality_model.pkl"
ENCODER_PATH = ROOT / "models" / "label_encoder.pkl"
FEATURES_PATH = ROOT / "models" / "feature_columns.pkl"

def load_artifacts():
    if not MODEL_PATH.exists():
        from train_model import train
        train()
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    feature_columns = joblib.load(FEATURES_PATH)
    return model, encoder, feature_columns

def predict_water_quality(input_dict):
    model, encoder, feature_columns = load_artifacts()
    row = pd.DataFrame([input_dict])
    for col in feature_columns:
        if col not in row.columns:
            row[col] = 0
    row = row[feature_columns]
    pred = model.predict(row)[0]
    label = encoder.inverse_transform([pred])[0]

    confidence = None
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(row)[0]
        confidence = float(max(probs))

    return label, confidence
