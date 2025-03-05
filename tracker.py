import csv
import os
from datetime import datetime

# File to store expense data
FILE_NAME = "expenses.csv"

# Ensure the CSV file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])

def add_expense():
    """Function to add an expense"""
    date = datetime.now().strftime("%Y-%m-%d")  # Auto-add today's date
    amount = input("Enter amount spent: ")
    category = input("Enter category (e.g., Food, Transport, Bills): ")
    description = input("Enter description: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("✅ Expense added successfully!")

def view_expenses():
    """Function to display all expenses"""
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))

def category_summary():
    """Function to summarize expenses by category"""
    expenses = {}
    
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category = row[2]
            amount = float(row[1])
            expenses[category] = expenses.get(category, 0) + amount

    print("\n📊 Expense Summary by Category:")
    for category, total in expenses.items():
        print(f"{category}: ${total:.2f}")

def monthly_summary():
    """Function to display expenses for a specific month"""
    month = input("Enter the month (YYYY-MM): ")
    
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        found = False
        print(f"\n📅 Expenses for {month}:")
        for row in reader:
            if row[0].startswith(month):
                print(", ".join(row))
                found = True

    if not found:
        print("❌ No expenses found for this month.")

def search_expense():
    """Function to search expenses by category or keyword"""
    keyword = input("Enter category or keyword to search: ").lower()
    
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        found = False
        print("\n🔍 Search Results:")
        for row in reader:
            if keyword in row[2].lower() or keyword in row[3].lower():
                print(", ".join(row))
                found = True

    if not found:
        print("❌ No matching expenses found.")

def delete_expense():
    """Function to delete an expense"""
    view_expenses()
    index = int(input("Enter the row number to delete (starting from 1): "))

    with open(FILE_NAME, mode="r") as file:
        rows = list(csv.reader(file))

    if 1 <= index < len(rows):
        del rows[index]
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("✅ Expense deleted successfully!")
    else:
        print("❌ Invalid row number.")

def export_expenses():
    """Function to export expenses as a CSV file"""
    export_file = "expense_report.csv"
    
    with open(FILE_NAME, "r") as infile, open(export_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerows(reader)
    
    print(f"📂 Expenses exported successfully to {export_file}!")

def main():
    """Main menu for the Expense Tracker"""
    while True:
        print("\n💰 Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Category Summary")
        print("4. View Monthly Summary")
        print("5. Search Expenses")
        print("6. Delete an Expense")
        print("7. Export Expenses")
        print("8. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            search_expense()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            export_expenses()
        elif choice == "8":
            print("👋 Exiting. Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
