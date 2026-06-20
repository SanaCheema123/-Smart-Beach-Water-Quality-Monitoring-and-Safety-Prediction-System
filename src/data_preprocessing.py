from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "beach_water_quality.csv"
PROCESSED_PATH = ROOT / "data" / "processed" / "processed_water_quality.csv"

TARGET_CANDIDATES = [
    "water_quality_status", "quality_status", "status", "class", "target",
    "beach_status", "swim_status"
]

def load_dataset(path=RAW_PATH):
    path = Path(path)
    if not path.exists():
        from generate_sample_data import main
        main()
    return pd.read_csv(path)

def clean_columns(df):
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_").replace("-", "_") for c in df.columns]
    return df

def clean_dataset(df):
    df = clean_columns(df)
    df = df.drop_duplicates()

    for col in df.columns:
        converted = pd.to_numeric(df[col], errors="coerce")
        if converted.notna().sum() > len(df) * 0.70:
            df[col] = converted.fillna(converted.median())
        else:
            mode_value = df[col].mode()
            df[col] = df[col].astype(str).replace("nan", None)
            df[col] = df[col].fillna(mode_value.iloc[0] if not mode_value.empty else "Unknown")
    return df

def ensure_target(df):
    df = df.copy()

    for c in TARGET_CANDIDATES:
        if c in df.columns:
            if c != "water_quality_status":
                df = df.rename(columns={c: "water_quality_status"})
            return df

    # Create educational target from water quality variables if Kaggle target is absent
    bacteria_col = next((c for c in df.columns if "bacteria" in c or "ecoli" in c or "e_coli" in c), None)
    turbidity_col = next((c for c in df.columns if "turbidity" in c), None)
    rainfall_col = next((c for c in df.columns if "rain" in c), None)

    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        raise ValueError("No numeric columns found. Please add water_quality_status column.")

    score = pd.Series(0, index=df.index, dtype=float)
    if bacteria_col:
        s = df[bacteria_col]
        score += (s - s.min()) / (s.max() - s.min() + 1e-9) * 0.55
    if turbidity_col:
        s = df[turbidity_col]
        score += (s - s.min()) / (s.max() - s.min() + 1e-9) * 0.25
    if rainfall_col:
        s = df[rainfall_col]
        score += (s - s.min()) / (s.max() - s.min() + 1e-9) * 0.20

    if score.sum() == 0:
        score = numeric.apply(lambda s: (s - s.min()) / (s.max() - s.min() + 1e-9)).mean(axis=1)

    df["water_quality_status"] = pd.cut(
        score, bins=[-0.01, 0.33, 0.66, 1.5],
        labels=["Safe", "Moderate Risk", "Unsafe"]
    ).astype(str)

    return df

def preprocess(path=RAW_PATH):
    df = load_dataset(path)
    df = clean_dataset(df)
    df = ensure_target(df)
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    return df

if __name__ == "__main__":
    df = preprocess()
    print(f"Processed data saved: {PROCESSED_PATH}")
    print(df.head())
