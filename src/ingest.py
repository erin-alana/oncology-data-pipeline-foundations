import pandas as pd

RAW_DATA_PATH = "data/raw/oncology_sample.csv"

def load_data(file_path):
    """Load oncology CSV data into a pandas DataFrame."""
    return pd.read_csv(file_path)

def main():
    df = load_data(RAW_DATA_PATH)

    print("Oncology data loaded successfully.")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumn names:")
    print(df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head())

if __name__ == "__main__":
    main()
