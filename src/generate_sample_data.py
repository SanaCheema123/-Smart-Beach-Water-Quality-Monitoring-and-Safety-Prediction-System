from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "beach_water_quality.csv"

def main():
    np.random.seed(42)
    n = 1500
    beaches = np.random.choice(["North Beach", "Palm Coast", "Blue Bay", "Silver Shore", "Coral Point"], n)
    water_temp = np.random.normal(24, 4, n).clip(10, 36)
    air_temp = water_temp + np.random.normal(3, 3, n)
    turbidity = np.random.gamma(2.2, 1.8, n).clip(0.1, 25)
    wave_height = np.random.gamma(1.8, 0.35, n).clip(0.05, 4)
    rainfall = np.random.gamma(1.4, 5, n).clip(0, 80)
    ph = np.random.normal(7.6, 0.35, n).clip(6.2, 8.8)
    dissolved_oxygen = np.random.normal(7.2, 1.2, n).clip(2, 12)
    conductivity = np.random.normal(42000, 6500, n).clip(15000, 60000)
    bacteria_count = (
        35 + turbidity * 9 + rainfall * 3.4 + wave_height * 18
        + np.random.normal(0, 35, n)
    ).clip(1, 1200)

    risk_score = (
        bacteria_count * 0.55 + turbidity * 16 + rainfall * 2.5
        + wave_height * 35 - dissolved_oxygen * 8
    )

    status = np.where(risk_score < 120, "Safe", np.where(risk_score < 260, "Moderate Risk", "Unsafe"))

    df = pd.DataFrame({
        "beach_name": beaches,
        "water_temperature": water_temp.round(2),
        "air_temperature": air_temp.round(2),
        "turbidity": turbidity.round(2),
        "wave_height": wave_height.round(2),
        "rainfall": rainfall.round(2),
        "ph": ph.round(2),
        "dissolved_oxygen": dissolved_oxygen.round(2),
        "conductivity": conductivity.round(2),
        "bacteria_count": bacteria_count.round(2),
        "water_quality_status": status
    })
    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(RAW_PATH, index=False)
    print(f"Sample dataset saved: {RAW_PATH}")

if __name__ == "__main__":
    main()
