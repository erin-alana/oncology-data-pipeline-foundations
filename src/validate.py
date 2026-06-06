import pandas as pd

RAW_DATA_PATH = "data/raw/oncology_sample.csv"
ALLOWED_STAGES = ["I", "II", "III", "IV"]

def validate_data(df):
    """Run basic oncology data quality checks."""
    results = {
        "total_rows": len(df),
        "duplicate_patient_ids": df["patient_id"].duplicated().sum(),
        "missing_stage": df["stage"].isna().sum(),
        "invalid_age_at_diagnosis": len(
            df[(df["age_at_diagnosis"] < 0) | (df["age_at_diagnosis"] > 120)]
        ),
        "invalid_stage": len(
            df[~df["stage"].isin(ALLOWED_STAGES) & df["stage"].notna()]
        )
    }

    return results

def main():
    df = pd.read_csv(RAW_DATA_PATH)
    results = validate_data(df)

    print("Data Quality Report")
    print("-------------------")
    for check, value in results.items():
        print(f"{check}: {value}")

if __name__ == "__main__":
    main()
