import sqlite3
import pandas as pd
import os

DATABASE_PATH = "database/oncology.db"
OUTPUT_PATH = "outputs/stage_summary.csv"

def main():
    os.makedirs("outputs", exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)

    query = """
    SELECT
        stage,
        COUNT(*) AS patient_count
    FROM patients
    GROUP BY stage
    ORDER BY patient_count DESC;
    """

    results = pd.read_sql_query(query, conn)

    print(results)

    results.to_csv(OUTPUT_PATH, index=False)

    conn.close()

    print(f"Stage summary saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()