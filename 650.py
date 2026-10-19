orders = [
    {"item": "Laptop", "category": "Electronics", "quantity": 3, "price": 40000, "status": "delivered"},
    {"item": "Desk", "category": "Furniture", "quantity": 5, "price": 12000, "status": "delivered"},
    {"item": "Shoes", "category": "Fashion", "quantity": 8, "price": 3000, "status": "delivered"},
    {"item": "Phone", "category": "Electronics", "quantity": 2, "price": 25000, "status": "cancelled"},
    {"item": "Chair", "category": "Furniture", "quantity": 2, "price": 8000, "status": "delivered"}
]

blocked_categories = ["Fashion"]

total_revenue = sum(
    order["quantity"] * order["price"]
    for order in orders
    if order["category"] not in blocked_categories
    and order["category"] != "cancelled"
    and(
        order["category"] == "Electronics"
        or order['quantity'] >= 4
    )
)

print(total_revenue)