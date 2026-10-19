expenses = [
    {"category": "Food", "amount": 3500, "status": "paid"},
    {"category": "Rent", "amount": 18000, "status": "paid"},
    {"category": "Travel", "amount": 15000, "status": "paid"},
    {"category": "Food", "amount": 1200, "status": "paid"},
    {"category": "Equipment", "amount": 9000, "status": "pending"}
]
blocked = ["Travel"]

total = sum(
    p["amount"]
    for p in expenses
    if p["category"] not in blocked
    and p["status"] == "paid"
    and (p["category"] == "Food" or p['amount'] >= 12000 )
    and not (p["category"] == "Food" and p["amount"] < 2000 )
)

print(total)