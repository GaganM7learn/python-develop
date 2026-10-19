expenses = [
    {"name": "Amazon", "category": "Shopping", "amount": 4500, "status": "approved"},
    {"name": "Swiggy", "category": "Food", "amount": 1200, "status": "approved"},
    {"name": "Uber", "category": "Travel", "amount": 1800, "status": "pending"},
    {"name": "Flipkart", "category": "Shopping", "amount": 3200, "status": "approved"},
    {"name": "Zomato", "category": "Food", "amount": 2500, "status": "approved"},
    {"name": "Hotel", "category": "Travel", "amount": 6000, "status": "approved"}
]

total_expenses = sum(
    expense["amount"]
    for expense in expenses 
    if ( expense['category'] == "Shopping" or expense['category'] == "Food") and ( expense["status"] == "approved" and expense["amount"] >= 2000)

)

print(total_expenses)