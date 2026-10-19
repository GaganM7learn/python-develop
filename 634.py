orders = [
    {"item": "Camera", "category": "Electronics", "quantity": 4, "price": 45000, "status": "completed"},
    {"item": "Sofa", "category": "Furniture", "quantity": 2, "price": 30000, "status": "completed"},
    {"item": "Printer", "category": "Electronics", "quantity": 5, "price": 12000, "status": "pending"},
    {"item": "Bookshelf", "category": "Furniture", "quantity": 6, "price": 7000, "status": "completed"},
    {"item": "Keyboard", "category": "Electronics", "quantity": 3, "price": 2500, "status": "cancelled"},
    {"item": "Cupboard", "category": "Furniture", "quantity": 4, "price": 15000, "status": "completed"}
]

total_order_value = sum(
    item["quantity"] * item["price"]
    for item in orders
    if (item["category"] == "Electronics" or item['category'] == "Furniture")
    and item["status"] == "completed"
    and item["quantity"] >= 4
)

print(total_order_value)