import sqlite3
import pandas as pd
import sqlite3
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# File Paths
DATA_PATH = "data/raw/ds_salaries.csv"

# Load Dataset
def load_data():
    """Loads the dataset into a Pandas DataFrame."""
    df = pd.read_csv(DATA_PATH)
    print("Dataset Loaded Successfully!")
    print("Columns:", df.columns.tolist())
    print("\nBasic Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    return df



DB_PATH = "data/raw/job_market.db"
def store_data_in_db(df):
    """Stores the cleaned DataFrame in an SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("job_salaries", conn, if_exists="replace", index=False)
    conn.close()
    print("Cleaned Data stored in SQLite successfully!")

