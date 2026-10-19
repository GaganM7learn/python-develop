expenses = [
    {"item": "Lunch", "amount": 150},
    {"item": "Bus", "amount": 40},
    {"item": "Book", "amount": 250}
]

def show_expenses(expenses):
    for expense in expenses:
       print(expense["item"] , expense["amount"])
       total = sum( expense["amount"] for expense in expenses )
    print("Total :" , total)
    pass



show_expenses(expenses)