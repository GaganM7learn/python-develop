orders = [
    {"item": "Laptop", "category": "Electronics", "amount": 70000, "status": "paid"},
    {"item": "Chair", "category": "Furniture", "amount": 9000, "status": "paid"},
    {"item": "Phone", "category": "Electronics", "amount": 40000, "status": "cancelled"},
    {"item": "Desk", "category": "Furniture", "amount": 15000, "status": "paid"},
    {"item": "Book", "category": "Stationery", "amount": 800, "status": "paid"}
]

blocked_categories = ["stationery" , "Furniture"]

total_orders = sum(
    order["amount"]
    for order in orders 
    if order["category"] not in blocked_categories
    and order["status"] == "paid"
    and order["amount"] >= 10000
)

print(total_orders)