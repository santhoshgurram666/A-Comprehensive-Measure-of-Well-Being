"""
Train a Linear Regression model to predict HDI scores and save artifacts.
"""

import pickle
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = ROOT / "Dataset" / "Human Development Index.csv"
MODEL_PATH = ROOT / "models" / "hdi_model.pkl"

FEATURE_INDICES = [2, 5, 6, 7, 8]
TARGET_INDEX = 4


def hdi_tier(score: float) -> str:
    if score >= 0.800:
        return "Very High"
    if score >= 0.700:
        return "High"
    if score >= 0.550:
        return "Medium"
    return "Low"


def main() -> None:
    df = pd.read_csv(DATASET_PATH)

    y = df.iloc[:, TARGET_INDEX]
    raw_x = df.iloc[:, FEATURE_INDICES].copy()

    label_encoder = LabelEncoder()
    feature_names = raw_x.columns.tolist()
    country_encoded = label_encoder.fit_transform(raw_x.iloc[:, 0].astype(str))

    x = pd.DataFrame({feature_names[0]: country_encoded})
    for column in feature_names[1:]:
        x[column] = pd.to_numeric(raw_x[column], errors="coerce")

    print("Null counts before fill:")
    print(x.isnull().sum())
    x = x.fillna(x.mean(numeric_only=True))

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    print("\nActual y_test values:")
    print(y_test.values)
    print("\nPredicted y_pred values:")
    print(y_pred)
    print(f"\nR-squared: {r2_score(y_test, y_pred):.4f}")
    print(f"MAE: {mean_absolute_error(y_test, y_pred):.4f}")

    sample = x_test.iloc[0:1]
    sample_pred = model.predict(sample)[0]
    print(f"\nSample prediction: {sample_pred:.3f} ({hdi_tier(sample_pred)})")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    artifacts = {
        "model": model,
        "label_encoder": label_encoder,
        "feature_indices": FEATURE_INDICES,
        "target_index": TARGET_INDEX,
        "feature_names": [
            "Country",
            "Life Expectancy at Birth",
            "Expected Years of Schooling",
            "Mean Years of Schooling",
            "GNI per Capita (PPP $)",
        ],
    }
    with open(MODEL_PATH, "wb") as file:
        pickle.dump(artifacts, file)

    print(f"\nModel saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
