import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import dill 
import os


def load_data():
    """Loads cleaned data from SQLite database."""
    conn = sqlite3.connect("data/raw/job_market.db")
    query = "SELECT * FROM job_salaries"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def preprocess_data(df):
    """Encodes categorical features and scales numerical features."""
    
    numerical_columns = ['work_year','salary','salary_in_usd','remote_ratio']
    categorical_columns = ['experience_level', 'employment_type', 'job_title', 'salary_currency', 'employee_residence', 'company_location', 'company_size']
    num_pipeline= Pipeline(
        steps=[
            ("imputer",SimpleImputer(strategy="median")),
            ("scaler",StandardScaler())
            ])

    cat_pipeline=Pipeline(
        steps=[
        ("imputer",SimpleImputer(strategy="most_frequent")),
        ("one_hot_encoder",OneHotEncoder()),
        ("scaler",StandardScaler(with_mean=False))
        ])
    preprocessor=ColumnTransformer(
        [   ("num_pipeline",num_pipeline,numerical_columns),
            ("cat_pipelines",cat_pipeline,categorical_columns)
        ])
    file_path = "data\\processed\\preprocessor.pkl"
    with open(file_path,"wb") as file_obj:
            dill.dump(preprocessor, file_obj)  

def split_data(df):
    """Splits data into training and testing sets."""
    X = df.drop(columns=['salary_in_usd'])
    y = df['salary_in_usd']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
