# -*- coding: utf-8 -*-
"""expense tracker.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YaczFqiluo1nAtNFI1SC-xOkBNavjPSN
"""

import csv
import os

# File to store expenses
FILE_NAME = "/content/expense_data.csv"

# Check if the file exists, if not, create it with a header
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Description", "Category", "Amount"])


def add_expense(date, description, category, amount):
    """
    Adds an expense to the CSV file.
    :param date: Date of the expense (YYYY-MM-DD).
    :param description: Brief description of the expense.
    :param category: Expense category (e.g., Food, Travel, Bills).
    :param amount: Amount spent.
    """
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])
    print("Expense added successfully!")


def view_expenses():
    """
    Reads and displays all expenses from the CSV file.
    """
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Expense List ---")
            for i, row in enumerate(reader):
                if i == 0:
                    print(f"{row[0]:<12} {row[1]:<20} {row[2]:<15} {row[3]:>10}")
                    print("-" * 60)
                else:
                    print(f"{row[0]:<12} {row[1]:<20} {row[2]:<15} {row[3]:>10}")
    else:
        print("No expenses found. Start by adding one!")


def expense_summary():
    """
    Displays the total expenses by category.
    """
    if os.path.exists(FILE_NAME):
        summary = {}
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row["Category"]
                amount = float(row["Amount"])
                summary[category] = summary.get(category, 0) + amount

        print("\n--- Expense Summary ---")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
    else:
        print("No expenses found. Start by adding one!")


def main():
    """
    Main function to interact with the user.
    """
    print("Expense Tracker")
    print("================")
    while True:
        print("\nOptions:")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. View Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ").strip()
            description = input("Enter description: ").strip()
            category = input("Enter category (e.g., Food, Travel, Bills): ").strip()
            amount = input("Enter amount: ").strip()

            if date and description and category and amount:
                try:
                    amount = float(amount)
                    add_expense(date, description, category, amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            else:
                print("All fields are required!")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()