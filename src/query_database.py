import sqlite3
import pandas as pd

DATABASE_PATH = "database/oncology.db"

def main():
    conn = sqlite3.connect(DATABASE_PATH)

    query = """
    SELECT
        stage,
        COUNT(*) AS patient_count
    FROM patients
    GROUP BY stage
    ORDER BY patient_count DESC
    """

    results = pd.read_sql_query(query, conn)

    print(results)

    conn.close()

if __name__ == "__main__":
    main()
