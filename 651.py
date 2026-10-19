purchases = [
    {"item": "Tablet", "category": "Electronics", "quantity": 4, "price": 18000, "status": "completed"},
    {"item": "Bookshelf", "category": "Furniture", "quantity": 6, "price": 9000, "status": "completed"},
    {"item": "Jacket", "category": "Fashion", "quantity": 7, "price": 2500, "status": "completed"},
    {"item": "Camera", "category": "Electronics", "quantity": 2, "price": 30000, "status": "cancelled"},
    {"item": "Dining Set", "category": "Furniture", "quantity": 3, "price": 14000, "status": "completed"},
    {"item": "Headphones", "category": "Electronics", "quantity": 5, "price": 6000, "status": "completed"}
]

blocked_categories = ["Fashion"]

total_purchase_value = sum(
    item['quantity'] * item["price"]
    for item in purchases
    if item["category"] not in blocked_categories
    and item["status"] != "cancelled"
    and (
        item["category"] == "Electronics" or item["quantity"] >= 5
    )
)

print(total_purchase_value)