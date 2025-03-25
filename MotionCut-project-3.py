import csv
import os
from datetime import datetime

data_file = "expenses.csv"

def add_expense(amount, category, description):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(data_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(data_file):
        print("No expenses recorded yet.")
        return
    
    print("\nExpense Records:")
    with open(data_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def expense_summary():
    if not os.path.exists(data_file):
        print("No expenses recorded yet.")
        return

    category_totals = {}
    total_expense = 0
    with open(data_file, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if not row:  # Skip empty lines
                continue
            date, amount, category, description = row
            try:
                amount = float(amount)
                total_expense += amount
                category_totals[category] = category_totals.get(category, 0) + amount
            except ValueError:
                print(f"Skipping invalid data: {row}")

    print("\nExpense Summary:")
    print(f"Total Expenses: ${total_expense:.2f}")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")


def main():
    if not os.path.exists(data_file):
        with open(data_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")
                add_expense(amount, category, description)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
