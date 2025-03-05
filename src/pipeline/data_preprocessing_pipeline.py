from src.components.data_preprocessing import load_data, preprocess_data, split_data

def run_data_preprocessing_pipeline():
    try:
        df = load_data()
        preprocess_data(df)
        X_train, X_test, y_train, y_test = split_data(df)
    except Exception as e:
        print("Error in data Preprocessing")
        
if __name__ == "__main__":
    run_data_preprocessing_pipeline()