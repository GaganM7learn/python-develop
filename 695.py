payments = [
    {"method": "Card", "amount": 5000, "status": "success"},
    {"method": "UPI", "amount": 12000, "status": "success"},
    {"method": "Cash", "amount": 20000, "status": "pending"}
]

total = sum(
    p["amount"]
    for p in payments
    if p["status"] == "success"
    and (p["method"] == "Card" or p["amount"] >= 10000)
)

print(total)