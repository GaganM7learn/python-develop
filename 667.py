goods = [
    {"name": "Tablet", "category": "Electronics", "revenue": 35000, "cost": 24000, "status": "sold"},
    {"name": "Sofa", "category": "Furniture", "revenue": 48000, "cost": 32000, "status": "sold"},
    {"name": "Shoes", "category": "Fashion", "revenue": 12000, "cost": 5000, "status": "sold"},
    {"name": "Camera", "category": "Electronics", "revenue": 22000, "cost": 15000, "status": "returned"},
    {"name": "Dining Table", "category": "Furniture", "revenue": 19000, "cost": 11000, "status": "sold"},
    {"name": "Headphones", "category": "Electronics", "revenue": 18000, "cost": 9000, "status": "sold"}
]

blocked_categories = ["Fashion"]

total_profit = sum(
    good["revenue"] - good["cost"]
    for good in goods
    if good["category"] not in blocked_categories
    and good["status"] == "sold"
    and (
        good["category"] == "Electronics"
        or good["revenue"] >= 20000
    )
)

print(total_profit)