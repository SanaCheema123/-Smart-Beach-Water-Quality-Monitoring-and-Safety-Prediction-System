from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
def main():
    comparison = ROOT / "outputs" / "model_comparison.csv"
    report = ROOT / "outputs" / "classification_report.txt"
    if comparison.exists():
        print(pd.read_csv(comparison))
    if report.exists():
        print(report.read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()
