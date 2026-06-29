"""
Flask web application for HDI score prediction.
"""

import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from flask import Flask, render_template, request

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "hdi_model.pkl"
DATASET_PATH = ROOT / "Dataset" / "Human Development Index.csv"

app = Flask(
    __name__,
    template_folder=str(ROOT / "templates"),
    static_folder=str(ROOT / "static"),
)


def hdi_tier(score: float) -> str:
    if score >= 0.800:
        return "Very High"
    if score >= 0.700:
        return "High"
    if score >= 0.550:
        return "Medium"
    return "Low"


def tier_message(tier: str) -> str:
    messages = {
        "Very High": (
            "Strong performance across health, education, and income places this "
            "country among the most developed nations."
        ),
        "High": (
            "Solid development outcomes with room for further gains in wellbeing "
            "and living standards."
        ),
        "Medium": (
            "Mid-range development. Improvements in healthcare, education, or income "
            "could significantly enhance human development outcomes."
        ),
        "Low": (
            "Development challenges identified. Targeted investments in health, "
            "education, and income generation are recommended."
        ),
    }
    return messages.get(tier, "")


def load_artifacts():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)


def load_countries() -> list[str]:
    df = pd.read_csv(DATASET_PATH)
    return sorted(df.iloc[:, 2].astype(str).unique())


artifacts = load_artifacts()
model = artifacts["model"]
label_encoder = artifacts["label_encoder"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction_text = None
    tier = None
    message = None

    if request.method == "POST":
        country = request.form["country"]
        life_expectancy = float(request.form["life_expectancy"])
        expected_schooling = float(request.form["expected_schooling"])
        mean_schooling = float(request.form["mean_schooling"])
        gni_per_capita = float(request.form["gni_per_capita"])

        country_encoded = label_encoder.transform([country])[0]
        features = np.array(
            [[country_encoded, life_expectancy, expected_schooling, mean_schooling, gni_per_capita]]
        )

        score = round(float(model.predict(features)[0]), 3)
        tier = hdi_tier(score)
        message = tier_message(tier)
        prediction_text = f"Predicted HDI Score: {score} ({tier} Human Development)"

    return render_template(
        "indexnew.html",
        countries=load_countries(),
        prediction_text=prediction_text,
        tier=tier,
        message=message,
    )


if __name__ == "__main__":
    app.run(debug=True)
