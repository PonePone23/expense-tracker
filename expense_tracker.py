from expense import Expense


def main():
    print(f"Running Expense Tracker")
    expense_file_path = "expense.csv"
    budget = 20000
    #Get user input for expense
    #expense = get_user_expense()
    #print(expense)

    #Write their expense to a file
    #save_expense_to_file(expense,expense_file_path)

    #Read file and summarize expenses
    summarize_expenses(expense_file_path,budget)

def get_user_expense():
    print(f"Getting user expense")
    expense_name = input("> Enter expense name")
    while True:
        try:
            expense_amount = float(input("> Enter expense amount: "))
        except:
            print("Your amount should be number")
            continue
        if not isinstance(expense_amount,str):
            break
    
    print(f"You entered {expense_name}, {expense_amount}")
    expense_categories = [
        "🍟 Food",
        "🏡 Home",
        "👩‍💻 Work",
        "🤩 Fun",
        "✨ Misc"
    ]
    while True:
        print("Select a category: ")
        for i, category in enumerate(expense_categories):
            print(f"{i+1}. {category}")
        value_range = f"[1 - {len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter a category number {value_range}: "))-1
        except Exception:
            continue
        if selected_index in range(len(expense_categories)):
            category_item = expense_categories[selected_index]
            new_expense = Expense(name=expense_name,category=category_item,amount=expense_amount)
            return new_expense
        else:
            print("Invalid category.Please Try again!")
        

def save_expense_to_file(expense: Expense,expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expenses(expense_file_path,budget):
    print("Summarizing user expense")
    expenses:Expense = []
    with open(expense_file_path,'r') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category,expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount),
                category=expense_category
            )
            print(line_expense)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print(amount_by_category)
    print("Expenses by category")
    for key,amount in amount_by_category.items():
        print(f"{key}: ${amount}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent ${total_spent:.2f} this month")

    remaining_budget = budget- total_spent
    print(f"Budget Remaining: ${remaining_budget:.2f}")


if __name__ == "__main__":
    main()