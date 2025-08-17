# model/load_model.py

import pickle

def load_xgboost_model():
    try:
        from xgboost import XGBRegressor
    except ImportError:
        raise ImportError("xgboost is required. Run: pip install xgboost")

    try:
        # Try loading tuned model from a pickle file
        with open("xgbr_tat_tuned.pkl", "rb") as f:
            model = pickle.load(f)
        print("Using tuned XGBoost model.")
    except FileNotFoundError:
        try:
            with open("xgbr_tat.pkl", "rb") as f:
                model = pickle.load(f)
            print("Using default XGBoost model.")
        except FileNotFoundError:
            print("Error: No trained XGBoost model found.")
            model = None
    return model
