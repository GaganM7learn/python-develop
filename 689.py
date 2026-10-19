inventory = [
    {"name": "Phone", "category": "Electronics", "revenue": 45000, "cost": 32000, "status": "sold"},
    {"name": "Jacket", "category": "Clothing", "revenue": 36000, "cost": 21000, "status": "sold"},
    {"name": "Table", "category": "Furniture", "revenue": 28000, "cost": 16000, "status": "sold"},
    {"name": "Headphones", "category": "Electronics", "revenue": 25000, "cost": 14000, "status": "sold"},
    {"name": "Camera", "category": "Electronics", "revenue": 38000, "cost": 26000, "status": "sold"},
    {"name": "Sofa", "category": "Furniture", "revenue": 42000, "cost": 30000, "status": "pending"}
]

blocked_categories = ["Clothing"]

total_profit = sum(
    inv['revenue'] - inv["cost"]
    for inv in inventory
    if inv["category"] not in blocked_categories
    and inv["status"] == "sold"
    and (
        inv["category"] == "Electronics"
        or inv["revenue"] >= 30000
    )
    and not (
        inv["category"] == "Electronics"
        and inv["revenue"] < 30000

    )
)

print(total_profit)