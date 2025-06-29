from datetime import datetime
from data import load_data

def summarize():
    """Generate a summary of total income, expenses, and balance."""
    df = load_data()
    income = df[df.Category == "Income"]["Amount"].sum()
    expense = df[df.Category == "Expense"]["Amount"].sum()
    print(f"Income: ₹{income:.2f}  Expenses: ₹{expense:.2f}  Balance: ₹{income - expense:.2f}")

def monthly_report(year=None, month=None):
    """Generate a monthly report."""
    df = load_data()
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    now = datetime.now()
    year = year or now.year
    month = month or now.month
    monthly_data = df[(df["Year"] == year) & (df["Month"] == month)]
    
    if monthly_data.empty:
        print("No transactions found for this period.")
        return
    
    print(f"\n📅 Monthly Report: {year}-{month:02d}")
    summary = monthly_data.groupby("Category")["Amount"].sum()
    print(summary.to_string())
    total = monthly_data["Amount"].sum()
    print(f"Total: ₹{total:.2f}")
