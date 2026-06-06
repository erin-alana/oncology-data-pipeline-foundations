import pandas as pd

RAW_DATA_PATH = "data/raw/oncology_sample.csv"
PROCESSED_DATA_PATH = "data/processed/oncology_cleaned.csv"

def transform_data(df):
    """Create derived oncology analytics fields."""
    df["is_advanced_stage"] = df["stage"].isin(["III", "IV"])
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 49, 64, 120],
        labels=["Under 50", "50-64", "65+"]
    )

    return df

def main():
    df = pd.read_csv(RAW_DATA_PATH)
    transformed_df = transform_data(df)
    transformed_df.to_csv(PROCESSED_DATA_PATH, index=False)

    print(f"Processed file saved to {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    main()
