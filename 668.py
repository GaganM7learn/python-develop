orders = [
    {"name": "Monitor", "category": "Electronics", "price": 18000, "quantity": 2, "status": "delivered"},
    {"name": "Chair", "category": "Furniture", "price": 7000, "quantity": 4, "status": "delivered"},
    {"name": "Jacket", "category": "Fashion", "price": 5000, "quantity": 3, "status": "delivered"},
    {"name": "Printer", "category": "Electronics", "price": 12000, "quantity": 1, "status": "pending"},
    {"name": "Table", "category": "Furniture", "price": 15000, "quantity": 2, "status": "delivered"}
]

blocked_categories = ["Fashion"]

total_value = sum(
    order["price"] * order['quantity']
    for order in orders
    if order["category"] not in blocked_categories
    and order["status"] == "delivered"
    and (
        order['category'] == "Electronics"
        or order["quantity"] >= 3
    )
)

print(total_value)