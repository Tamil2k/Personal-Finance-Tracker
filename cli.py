from datetime import datetime
from data import add_transaction
from reports import summarize, monthly_report
from budget import check_budget

def add_transaction_cli():
    """Add a transaction to the CSV."""
    date = input("Date dd-mm-yyyy hh:mm:ss ") or datetime.now().date().isoformat()
    desc = input("Description: Salary/Rent/Groceries: ")
    cat = input("Category (Income/Expense/...): ").title()
    amt = float(input("Amount: "))
    add_transaction(date, desc, cat, amt)

def show_summary():
    """Show the financial summary (Income, Expenses, Balance)."""
    summarize()

def show_monthly_report():
    """Show monthly report."""
    year = int(input("Year (or press enter for current year): ") or datetime.now().year)
    month = int(input("Month (1-12, or press enter for current month): ") or datetime.now().month)
    monthly_report(year, month)

def check_budget_alert():
    """Check for any budget overages."""
    year = int(input("Year (or press enter for current year): ") or datetime.now().year)
    month = int(input("Month (1-12, or press enter for current month): ") or datetime.now().month)
    check_budget(year, month)

def main():
    while True:
        print("\n1) Add Transaction\n2) Summary\n3) Monthly Report\n4) Budget Check\n5) Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_transaction_cli()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_monthly_report()
        elif choice == "4":
            check_budget_alert()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
