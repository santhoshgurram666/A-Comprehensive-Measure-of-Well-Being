"""
Exploratory data analysis and visualizations for the HDI dataset.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = ROOT / "Dataset" / "Human Development Index.csv"
STATIC_DIR = ROOT / "static"
STATIC_DIR.mkdir(parents=True, exist_ok=True)


def load_dataset() -> pd.DataFrame:
    return pd.read_csv(DATASET_PATH)


def main() -> None:
    df = load_dataset()

    print("Dataset shape:", df.shape)
    print("\nFirst five rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    print("\nNull counts (selected columns):")
    print(df.iloc[:, [2, 4, 5, 6, 7, 8]].isnull().sum())

    data1 = df.head(20)

    countries = df.iloc[:, 2].unique()
    print(f"\nUnique countries: {len(countries)}")
    print("Sample countries:", countries[:10])

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(10, 6))
    sns.stripplot(x=data1.iloc[:, 7], y=data1.iloc[:, 4])
    plt.xlabel("Mean Years of Schooling")
    plt.ylabel("HDI Score")
    plt.title("Mean Years of Schooling vs HDI")
    plt.tight_layout()
    plt.savefig(STATIC_DIR / "mean_schooling_vs_hdi.png", dpi=120)
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.stripplot(x=data1.iloc[:, 5], y=data1.iloc[:, 4])
    plt.xlabel("Life Expectancy at Birth")
    plt.ylabel("HDI Score")
    plt.title("Life Expectancy vs HDI")
    plt.tight_layout()
    plt.savefig(STATIC_DIR / "life_expectancy_vs_hdi.png", dpi=120)
    plt.close()

    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(14, 10))
    sns.heatmap(numeric_df.corr(), cmap="coolwarm", center=0)
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(STATIC_DIR / "correlation_heatmap.png", dpi=120)
    plt.close()

    print("\nVisualizations saved to static/")


if __name__ == "__main__":
    main()
