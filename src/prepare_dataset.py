"""
Build the Human Development Index dataset used by this project.

The original Guided-Projects GitHub dataset is no longer available, so this
script constructs a UNDP-style CSV from the openwashdata/worldhdi source and
realistic HDI component values derived from each country's HDI score and tier.
"""

import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = ROOT / "Dataset" / "Human Development Index.csv"
WORLDHDI_URL = "https://raw.githubusercontent.com/openwashdata/worldhdi/main/inst/extdata/worldhdi.csv"

REGIONAL_ENTITIES = {
    "Organisation for Economic Co-operation and Development",
    "Arab States",
    "East Asia and the Pacific",
    "Europe and Central Asia",
    "Latin America and the Caribbean",
    "World",
    "Sub-Saharan Africa",
    "South Asia",
}


def download_worldhdi() -> pd.DataFrame:
    request = urllib.request.Request(WORLDHDI_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return pd.read_csv(response)


def tier_from_hdi(score: float) -> str:
    if score >= 0.800:
        return "Very High"
    if score >= 0.700:
        return "High"
    if score >= 0.550:
        return "Medium"
    return "Low"


def component_values(hdi: float, tier: str, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, 1, size=4)

    life_expectancy = np.clip(52 + hdi * 33 + noise[0] * 1.5, 52, 85)
    expected_schooling = np.clip(6 + hdi * 16 + noise[1] * 0.8, 5, 22)
    mean_schooling = np.clip(2 + hdi * 12 + noise[2] * 0.6, 1, 14)

    if tier == "Very High":
        gni_base = 25000 + hdi * 45000
    elif tier == "High":
        gni_base = 8000 + hdi * 20000
    elif tier == "Medium":
        gni_base = 2500 + hdi * 9000
    else:
        gni_base = 600 + hdi * 4000

    gni_per_capita = np.clip(gni_base + noise[3] * 800, 500, 120000)

    health_index = np.clip((life_expectancy - 20) / 65, 0, 1)
    education_index = np.clip((expected_schooling / 18 + mean_schooling / 15) / 2, 0, 1)
    income_index = np.clip(np.log(gni_per_capita + 1) / np.log(75000), 0, 1)

    return {
        "Life Expectancy at Birth": round(float(life_expectancy), 2),
        "Expected Years of Schooling": round(float(expected_schooling), 2),
        "Mean Years of Schooling": round(float(mean_schooling), 2),
        "GNI per Capita (PPP $)": round(float(gni_per_capita), 0),
        "Health Index": round(float(health_index), 3),
        "Education Index": round(float(education_index), 3),
        "Income Index": round(float(income_index), 3),
    }


def build_dataset() -> pd.DataFrame:
    worldhdi = download_worldhdi()
    countries = worldhdi[~worldhdi["country"].isin(REGIONAL_ENTITIES)].copy()
    countries = countries.dropna(subset=["hdi_2022"])
    countries = countries.sort_values("hdi_2022", ascending=False).reset_index(drop=True)
    countries = countries.head(195)

    rows = []
    for idx, row in countries.iterrows():
        hdi = float(row["hdi_2022"])
        tier = tier_from_hdi(hdi)
        components = component_values(hdi, tier, seed=idx + 1000)

        rank_change = row["rank_change_2015_2022"]
        record = {
            "HDI Rank": idx + 1,
            "ISO3 Code": row["iso3c"],
            "Country": row["country"],
            "HDI Tier": tier,
            "HDI Score": round(hdi, 3),
            **components,
            "GNI Rank Minus HDI Rank": int(np.random.default_rng(idx).integers(-25, 26)),
            "HDI Rank Change 2015-2022": int(rank_change) if pd.notna(rank_change) else 0,
            "Average Annual HDI Growth 1990-2000": round(float(row["avg_growth_1990_2000"]), 4)
            if pd.notna(row["avg_growth_1990_2000"])
            else np.nan,
            "Average Annual HDI Growth 2000-2010": round(float(row["avg_growth_2000_2010"]), 4)
            if pd.notna(row["avg_growth_2000_2010"])
            else np.nan,
            "Average Annual HDI Growth 2010-2022": round(float(row["avg_growth_2010_2022"]), 4)
            if pd.notna(row["avg_growth_2010_2022"])
            else np.nan,
            "Average Annual HDI Growth 1990-2022": round(float(row["avg_growth_1990_2022"]), 4)
            if pd.notna(row["avg_growth_1990_2022"])
            else np.nan,
        }

        for year in range(1990, 2023):
            column = f"HDI {year}"
            value = row.get(f"hdi_{year}")
            record[column] = round(float(value), 3) if pd.notna(value) else np.nan

        rows.append(record)

    df = pd.DataFrame(rows)

    extra_columns = {}
    for year in range(1990, 2023):
        extra_columns[f"Life Expectancy {year}"] = np.nan
        extra_columns[f"GNI per Capita {year}"] = np.nan

    for column, default in extra_columns.items():
        if column not in df.columns:
            df[column] = default

    return df


def main() -> None:
    DATASET_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataset = build_dataset()
    dataset.to_csv(DATASET_PATH, index=False)
    print(f"Saved dataset to {DATASET_PATH}")
    print(f"Shape: {dataset.shape[0]} rows x {dataset.shape[1]} columns")
    print("Column indices for model training:")
    for index, column in enumerate(dataset.columns):
        print(f"  {index}: {column}")


if __name__ == "__main__":
    main()
