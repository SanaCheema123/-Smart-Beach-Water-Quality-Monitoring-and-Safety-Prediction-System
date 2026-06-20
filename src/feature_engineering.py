def add_features(df):
    df = df.copy()
    if "water_temperature" in df.columns and "air_temperature" in df.columns:
        df["temperature_gap"] = df["air_temperature"] - df["water_temperature"]
    if "turbidity" in df.columns and "rainfall" in df.columns:
        df["pollution_pressure_index"] = df["turbidity"] * 0.6 + df["rainfall"] * 0.4
    return df
