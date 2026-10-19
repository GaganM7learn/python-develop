orders = [
    {"name": "A", "category": "Electronics", "amount": 25000, "status": "completed"},
    {"name": "B", "category": "Furniture", "amount": 18000, "status": "completed"},
    {"name": "C", "category": "Fashion", "amount": 30000, "status": "completed"},
    {"name": "D", "category": "Electronics", "amount": 12000, "status": "pending"},
    {"name": "E", "category": "Books", "amount": 8000, "status": "completed"},
    {"name": "F", "category": "Furniture", "amount": 22000, "status": "completed"}
]

blocked_categories = ["Fashion", "Books"]

total_amount = sum(
    order["amount"]
    for order in orders
    if order["category"] not in blocked_categories
    and order["status"] == "completed"
    and (
        order["category"] == "Electronics"
        or order["amount"] >= 20000
    )
)

print(total_amount)
