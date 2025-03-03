import sqlite3

# Store in SQLite Database

DB_PATH = "data/sqlite_db/job_market.db"
def store_data_in_db(df):
    """Stores the cleaned DataFrame in an SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("job_salaries", conn, if_exists="replace", index=False)
    conn.close()
    print("Cleaned Data stored in SQLite successfully!")

