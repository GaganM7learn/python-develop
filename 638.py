expenses = [
    {"name": "Netflix", "category": "Entertainment", "amount": 1200, "status": "paid"},
    {"name": "Amazon", "category": "Shopping", "amount": 6500, "status": "paid"},
    {"name": "Uber", "category": "Travel", "amount": 3200, "status": "paid"},
    {"name": "Swiggy", "category": "Food", "amount": 4500, "status": "pending"},
    {"name": "Flipkart", "category": "Shopping", "amount": 8200, "status": "paid"},
    {"name": "BookMyShow", "category": "Entertainment", "amount": 2500, "status": "paid"}
]

blocked_categories = ["Entertainment" , "Food"]

total_allowed_expenses = sum(
    order["amount"]
    for order in expenses 
    if  order["category"] not in blocked_categories
    and order["status"] == "paid"
    and order["amount"] >= 3000
)

print(total_allowed_expenses)