products = [
    {"name": "Phone", "category": "Electronics", "revenue": 42000, "cost": 30000, "status": "sold"},
    {"name": "Desk", "category": "Furniture", "revenue": 24000, "cost": 15000, "status": "sold"},
    {"name": "Shoes", "category": "Fashion", "revenue": 32000, "cost": 18000, "status": "sold"},
    {"name": "Tablet", "category": "Electronics", "revenue": 22000, "cost": 16000, "status": "sold"},
    {"name": "Cabinet", "category": "Furniture", "revenue": 28000, "cost": 19000, "status": "pending"},
    {"name": "Camera", "category": "Electronics", "revenue": 35000, "cost": 24000, "status": "sold"}
]

blocked_categories = ["Fashion"]
total_profit = sum(
    pro["revenue"] - pro["cost"]
    for pro in products
    if pro["category"] not in blocked_categories
    and  pro["status"] == "sold"
    and (
        pro["category"] == "Electronics"
        or pro["revenue"] >= 25000
    )
    and not (
        pro["category"] == "Electronics"
        and pro["revenue"] < 25000

    )
)
print(total_profit)