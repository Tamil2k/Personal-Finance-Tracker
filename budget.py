from datetime import datetime
from data import load_data

# Define your monthly budget limits
BUDGET_LIMITS = {
    "Food": 3000,
    "Transport": 1000,
    "Shopping": 2000,
    "Expense": 5000
}

def check_budget(year=None, month=None):
    """Check for any budget overages in the current month."""
    df = load_data()
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    now = datetime.now()
    year = year or now.year
    month = month or now.month
    current_month_data = df[(df["Year"] == year) & (df["Month"] == month)]
    
    spent = current_month_data.groupby("Category")["Amount"].sum().to_dict()
    print("\n🚨 Budget Alerts:")
    for category, limit in BUDGET_LIMITS.items():
        actual_spent = spent.get(category, 0)
        if actual_spent > limit:
            print(f"⚠️ Over budget for {category}: Spent ₹{actual_spent:.2f} / Limit ₹{limit:.2f}")
        else:
            print(f"✅ {category}: ₹{actual_spent:.2f} / ₹{limit:.2f}")
