products = [
    {"name": "Laptop", "category": "Electronics", "quantity": 2, "price": 45000, "status": "sold"},
    {"name": "Sofa", "category": "Furniture", "quantity": 5, "price": 12000, "status": "sold"},
    {"name": "Shirt", "category": "Fashion", "quantity": 10, "price": 2000, "status": "sold"},
    {"name": "Phone", "category": "Electronics", "quantity": 1, "price": 30000, "status": "pending"},
    {"name": "Table", "category": "Furniture", "quantity": 3, "price": 15000, "status": "sold"},
    {"name": "Headphones", "category": "Electronics", "quantity": 4, "price": 5000, "status": "sold"}
]

blocked_categories = ["Fashion"]

total_value = sum(
    item['quantity'] * item["price"]
    for item in products
    if item["category"] not in blocked_categories
    and (
        item["category"] == 'Electronics' or item["quantity"] >= 4
    )
    and item["status"] == "sold"
)


print(total_value)