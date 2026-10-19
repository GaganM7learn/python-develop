items = [
    {"name": "Laptop", "category": "Electronics", "revenue": 50000, "cost": 35000, "status": "sold"},
    {"name": "Ball", "category": "Toys", "revenue": 5000, "cost": 2000, "status": "sold"},
    {"name": "Chair", "category": "Furniture", "revenue": 25000, "cost": 15000, "status": "sold"},
    {"name": "Monitor", "category": "Electronics", "revenue": 30000, "cost": 22000, "status": "pending"}
]

blocked_categories = ["Toys"]

total_profit = sum(
    item["revenue"] - item["cost"]
    for item in items
    if item["category"] not in blocked_categories
    and item["status"] == "sold"
    and item["revenue"] >= 20000
)

print(total_profit)