transactions = [
    {"name": "Phone", "category": "Electronics", "amount": 28000, "status": "approved"},
    {"name": "Sofa", "category": "Furniture", "amount": 42000, "status": "approved"},
    {"name": "Jacket", "category": "Fashion", "amount": 18000, "status": "approved"},
    {"name": "Tablet", "category": "Electronics", "amount": 15000, "status": "rejected"},
    {"name": "Dining Table", "category": "Furniture", "amount": 25000, "status": "approved"},
    {"name": "Headphones", "category": "Electronics", "amount": 35000, "status": "approved"}
]

blocked_status = ["rejected", "cancelled"]

total_transactions = sum(
    item["amount"]
    for item in transactions
    if item["status"] not in blocked_status
    and (
        item["category"] == "Electronics" or item["amount"] >= 30000
    )
)


print(total_transactions)