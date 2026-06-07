import pandas as pd
import os

RAW_DATA_PATH = "data/raw/oncology_sample.csv"
PROCESSED_DATA_PATH = "data/processed/oncology_cleaned.csv"
ERROR_DATA_PATH = "data/errors/oncology_validation_errors.csv"

ALLOWED_STAGES = ["I", "II", "III", "IV"]

def transform_data(df):
    """Clean oncology data and quarantine invalid records."""

    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("data/errors", exist_ok=True)

    invalid_records = df[
        df["stage"].isna()
        | ~df["stage"].isin(ALLOWED_STAGES)
        | (df["age_at_diagnosis"] < 0)
        | (df["age_at_diagnosis"] > 120)
        | df["patient_id"].duplicated()
    ].copy()

    cleaned_df = df.drop(invalid_records.index).copy()

    cleaned_df["is_advanced_stage"] = cleaned_df["stage"].isin(["III", "IV"])

    cleaned_df["age_group_at_diagnosis"] = pd.cut(
        cleaned_df["age_at_diagnosis"],
        bins=[0, 49, 64, 120],
        labels=["Under 50", "50-64", "65+"]
    )

    return cleaned_df, invalid_records

def main():
    df = pd.read_csv(RAW_DATA_PATH)

    cleaned_df, invalid_records = transform_data(df)

    cleaned_df.to_csv(PROCESSED_DATA_PATH, index=False)
    invalid_records.to_csv(ERROR_DATA_PATH, index=False)

    print(f"Cleaned data saved to {PROCESSED_DATA_PATH}")
    print(f"Validation errors saved to {ERROR_DATA_PATH}")
    print(f"Cleaned records: {len(cleaned_df)}")
    print(f"Quarantined records: {len(invalid_records)}")

if __name__ == "__main__":
    main()