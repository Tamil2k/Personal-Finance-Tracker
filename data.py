import pandas as pd
from datetime import datetime

CSV_FILE = "transactions.csv"

def load_data():
    """Load transaction data from CSV."""
    df = pd.read_csv(CSV_FILE, parse_dates=["Date"])
    df["Category"] = df["Category"].str.strip().str.title()
    return df

def save_data(df):
    """Save DataFrame to CSV."""
    df.to_csv(CSV_FILE, index=False)

def add_transaction(date, desc, cat, amt):
    """Add a new transaction to the CSV."""
    df = load_data()
    new = pd.DataFrame([[date, desc, cat, amt]], columns=df.columns)
    df = pd.concat([df, new], ignore_index=True)
    save_data(df)
