from pathlib import Path
import sys
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

try:
    from xgboost import XGBClassifier
    HAS_XGB = True
except Exception:
    HAS_XGB = False

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))
from data_preprocessing import preprocess

MODELS_DIR = ROOT / "models"
OUTPUTS_DIR = ROOT / "outputs"

def train():
    df = preprocess()

    target = "water_quality_status"
    X = df.drop(columns=[target])
    y = df[target].astype(str)

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    numeric_features = X.select_dtypes(include="number").columns.tolist()
    categorical_features = X.select_dtypes(exclude="number").columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )

    models = {
        "Decision Tree": DecisionTreeClassifier(max_depth=8, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=220, random_state=42, class_weight="balanced"),
    }

    if HAS_XGB:
        models["XGBoost"] = XGBClassifier(
            n_estimators=180,
            max_depth=5,
            learning_rate=0.08,
            subsample=0.9,
            colsample_bytree=0.9,
            eval_metric="mlogloss",
            random_state=42
        )

    stratify = y_encoded if len(set(y_encoded)) > 1 else None
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=stratify
    )

    MODELS_DIR.mkdir(exist_ok=True)
    OUTPUTS_DIR.mkdir(exist_ok=True)

    results = []
    best_name, best_score, best_pipeline = None, -1, None
    best_report, best_cm = None, None

    for name, model in models.items():
        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ])
        pipeline.fit(X_train, y_train)
        preds = pipeline.predict(X_test)

        acc = accuracy_score(y_test, preds)
        precision = precision_score(y_test, preds, average="weighted", zero_division=0)
        recall = recall_score(y_test, preds, average="weighted", zero_division=0)
        f1 = f1_score(y_test, preds, average="weighted", zero_division=0)

        results.append({
            "Model": name,
            "Accuracy": round(acc, 4),
            "Precision": round(precision, 4),
            "Recall": round(recall, 4),
            "F1 Score": round(f1, 4)
        })

        joblib.dump(pipeline, MODELS_DIR / f"{name.lower().replace(' ', '_')}_model.pkl")

        if acc > best_score:
            best_name, best_score, best_pipeline = name, acc, pipeline
            best_report = classification_report(y_test, preds, target_names=label_encoder.classes_, zero_division=0)
            best_cm = confusion_matrix(y_test, preds)

    joblib.dump(best_pipeline, MODELS_DIR / "best_water_quality_model.pkl")
    joblib.dump(label_encoder, MODELS_DIR / "label_encoder.pkl")
    joblib.dump(list(X.columns), MODELS_DIR / "feature_columns.pkl")

    pd.DataFrame(results).to_csv(OUTPUTS_DIR / "model_comparison.csv", index=False)
    (OUTPUTS_DIR / "classification_report.txt").write_text(best_report, encoding="utf-8")
    pd.DataFrame(best_cm, index=label_encoder.classes_, columns=label_encoder.classes_).to_csv(OUTPUTS_DIR / "confusion_matrix.csv")

    print(f"Best model: {best_name} | Accuracy: {best_score:.4f}")
    print(f"Model saved: {MODELS_DIR / 'best_water_quality_model.pkl'}")

if __name__ == "__main__":
    train()
