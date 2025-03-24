#Helper Functions for Data Processing

import pandas as pd

def load_data(filepath):
    """Loads the flight landing dataset."""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Renames columns for time series forecasting."""
    df = df.rename(columns={"Activity_Period": "ds", "Landing_Count": "y"})
    df["ds"] = pd.to_datetime(df["ds"], format="%Y")
    return df
