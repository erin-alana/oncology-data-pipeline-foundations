import sqlite3
import pandas as pd

DATABASE_PATH = "database/oncology.db"
DATA_PATH = "data/processed/oncology_cleaned.csv"

def main():
    conn = sqlite3.connect(DATABASE_PATH)

    df = pd.read_csv(DATA_PATH)

    df.to_sql(
        "patients",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Data loaded into SQLite database.")

if __name__ == "__main__":
    main()
