import sqlite3
import pandas as pd
import os

DATABASE_PATH = "database/oncology.db"
DATA_PATH = "data/processed/oncology_cleaned.csv"

def main():
    os.makedirs("database", exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    conn = sqlite3.connect(DATABASE_PATH)

    df.to_sql(
        "patients",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Data loaded into SQLite database.")
    print(f"Database created at: {DATABASE_PATH}")

if __name__ == "__main__":
    main()
