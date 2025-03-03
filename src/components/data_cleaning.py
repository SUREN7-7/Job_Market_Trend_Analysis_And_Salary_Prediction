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

# Data Cleaning & Preprocessing
def clean_data(df):

    """Cleans and preprocesses the dataset."""

    df = df.drop_duplicates().dropna()

    categorical_cols = ['experience_level', 'employment_type', 'company_size', 'remote_ratio']
    for col in categorical_cols:
        df[col] = df[col].astype('category').cat.codes

    
    # Normalize salary column using MinMaxScaler
    scaler = StandardScaler()
    df[['salary_in_usd']] = scaler.fit_transform(df[['salary_in_usd']])
    
    print("Data Cleaning & Preprocessing Completed!")
    print("\nUpdated Data Info:")
    print(df.info())
    return df