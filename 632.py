warehouse = [
    {"name": "Monitor", "category": "Electronics", "quantity": 5, "price": 15000},
    {"name": "Table", "category": "Furniture", "quantity": 2, "price": 7000},
    {"name": "Headphones", "category": "Electronics", "quantity": 8, "price": 3000},
    {"name": "Cabinet", "category": "Furniture", "quantity": 4, "price": 6000},
    {"name": "Pen", "category": "Stationery", "quantity": 20, "price": 30},
    {"name": "Speaker", "category": "Electronics", "quantity": 3, "price": 4500}
]

total_warehouse_value = sum(
    item["quantity"] * item['price']
    for item in warehouse
    if (item["category"] == "Electronics" or item["category"] == "Furniture") and item["quantity"] >= 3 )
print(total_warehouse_value)