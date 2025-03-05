import pandas as pd
from src.components.data_ingestion import load_data, store_data_in_db

def run_data_pipeline():
    """Runs the full data pipeline: cleaning data and storing it in the database."""
    try:
        # Clean the data
        df = load_data()
        
        # Store cleaned data in the database
        store_data_in_db(df)
        
        print("Data pipeline executed successfully!")
    except Exception as e:
        print("Error in data pipeline:", e)



if __name__ == "__main__":
    run_data_pipeline()
#python -m src.pipeline.data_pipeline 
#Stores the cleaned data in db
