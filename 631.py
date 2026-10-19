inventory = [
    {"name": "Keyboard", "category": "Electronics", "quantity": 4, "price": 2500},
    {"name": "Chair", "category": "Furniture", "quantity": 3, "price": 5000},
    {"name": "Mouse", "category": "Electronics", "quantity": 6, "price": 1200},
    {"name": "Desk", "category": "Furniture", "quantity": 2, "price": 9000},
    {"name": "Notebook", "category": "Stationery", "quantity": 10, "price": 150},
    {"name": "Lamp", "category": "Electronics", "quantity": 5, "price": 1800}
]

total_value = sum(
    item["quantity"] * item["price"]
    for item in inventory
    if (item["category"] == "Electronics" or item["category"] == "Furniture") and item['quantity'] >= 3
)

print(total_value)