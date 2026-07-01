print("Welcome to the Budget Tracker, where you can monitor your monthly expenses and savings!")

name = input("Enter your name: ")

monthly_income = float(input("What is your monthly income?: "))
rent_expense = float(input("What is your monthly expense on your rent?: "))
food_expense = float(input("What is your monthly expense on your food?: "))
travel_expense = float(input("What is your monthly expense on your travel?: "))

print(f"Name: {name}")
total_expense = rent_expense + food_expense + travel_expense
print(f"Monthly expenses: {total_expense}.")

savings = monthly_income - total_expense
print(f"Monthly savings: {savings}.")

savings_percentage = round((savings / monthly_income) * 100, 2)
print(f"Savings percentage: {savings_percentage}%.")

if savings_percentage >= 20:
    print("You are saving enough money!")
else:
    print("You need to save more money!")

