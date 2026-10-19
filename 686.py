sales = [
    {"name": "A", "category": "Electronics", "revenue": 30000, "cost": 21000, "status": "sold"},
    {"name": "B", "category": "Furniture", "revenue": 18000, "cost": 12000, "status": "sold"},
    {"name": "C", "category": "Fashion", "revenue": 25000, "cost": 15000, "status": "sold"},
    {"name": "D", "category": "Electronics", "revenue": 20000, "cost": 16000, "status": "pending"},
    {"name": "E", "category": "Furniture", "revenue": 28000, "cost": 17000, "status": "sold"}
]

blocked_categories = ["Fashion"]

total_profit = sum(
    sale["revenue"] - sale["cost"]
    for sale in sales
    if sale["category"] not in blocked_categories
    and sale["status"] == "sold"
    and (
        sale["category"] == "Electronics"
        or sale["revenue"] >= 25000
    )
    and not (
        sale["category"] == "Electronics"
        and sale["revenue"] < 25000
    )
)

print(total_profit)