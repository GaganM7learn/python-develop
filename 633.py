deliveries = [
    {"item": "Phone", "category": "Electronics", "quantity": 3, "price": 30000, "status": "delivered"},
    {"item": "Desk", "category": "Furniture", "quantity": 2, "price": 8000, "status": "delivered"},
    {"item": "Laptop", "category": "Electronics", "quantity": 1, "price": 70000, "status": "pending"},
    {"item": "Chair", "category": "Furniture", "quantity": 5, "price": 4000, "status": "delivered"},
    {"item": "Tablet", "category": "Electronics", "quantity": 4, "price": 20000, "status": "cancelled"}
]

total_delivery_value = sum(
    delivery["quantity"] * delivery["price"]
    for delivery in deliveries
    if (delivery["category"] == "Electronics" or delivery["category"] == "Furniture")
    and delivery["status"] == "delivered"
    and delivery['quantity'] >= 3
)
print(total_delivery_value)