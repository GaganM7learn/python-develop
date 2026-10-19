products = [
    {"name": "Laptop", "category": "Electronics", "revenue": 60000, "cost": 42000, "status": "sold"},
    {"name": "Desk", "category": "Furniture", "revenue": 25000, "cost": 16000, "status": "sold"},
    {"name": "Shirt", "category": "Fashion", "revenue": 8000, "cost": 3000, "status": "returned"},
    {"name": "Phone", "category": "Electronics", "revenue": 40000, "cost": 28000, "status": "sold"},
    {"name": "Bookshelf", "category": "Furniture", "revenue": 18000, "cost": 12000, "status": "sold"}
]

blocked_categories = ["Fashion"]
total_profit = sum(
    product["revenue"] - product["cost"]
    for product in products
    if product["category"] not in blocked_categories
    and product["status"] == "sold"
    and (
        product["category"] == "Electronics"
        or product["revenue"] >= 20000
    )

)

print(total_profit)