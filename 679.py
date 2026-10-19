purchases = [
    {"name": "P1", "category": "Appliances", "amount": 16000, "status": "approved"},
    {"name": "P2", "category": "Furniture", "amount": 27000, "status": "approved"},
    {"name": "P3", "category": "Groceries", "amount": 12000, "status": "approved"},
    {"name": "P4", "category": "Appliances", "amount": 9000, "status": "pending"},
    {"name": "P5", "category": "Clothing", "amount": 23000, "status": "approved"},
    {"name": "P6", "category": "Furniture", "amount": 14000, "status": "approved"},
    {"name": "P7", "category": "Appliances", "amount": 21000, "status": "approved"}
]

blocked_categories = ["Groceries", "Clothing"]

total_amount = sum(
    exp["amount"]
    for exp in purchases
    if exp["category"] not in blocked_categories
    and exp["status"] == "approved"
    and (
        exp["category"] == "Appliances"
        or exp["amount"] >= 20000
    )
)
print(total_amount)