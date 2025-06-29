# Personal-Finance-Tracker

Overview & Design Goals
This tracker is built for simplicity, modularity, and maintainability. It consists of four distinct modules, each with a clear responsibility:

data.py: Handles reading from and writing to the CSV file.

reports.py: Computes summaries and monthly breakdowns.

budget.py: Checks spending against predefined budgets and alerts the user.

cli.py: Presents a friendly command-line interface that ties everything together.


data.py
Centralizes all data interactions:

load_data() – reads and normalizes CSV into a Pandas DataFrame.

save_data() – persists DataFrame back to the CSV.

add_transaction() – appends a new transaction row.



reports.py
Focuses on analysis:

summarize() – calculates total income, expenses, and overall balance.

monthly_report(year, month) – filters transactions for a specific month and displays category-level spending plus totals.



budget.py
Implements a simple budget check:

check_budget(year, month) – sums spending by category, compares it to predefined limits, and prints alerts for overages.

Budget limits are centralized in a dictionary for easy adjustment. 

cli.py
Serves as the user interface, coordinating the modules:

Defines explicit functions for each user action (add_transaction_cli, show_summary, show_monthly_report, check_budget_alert).

main() manages a clear, looped menu: add, summary, monthly report, budget check, or quit.

