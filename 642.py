payments = [
    {"name": "A", "type": "Online", "amount": 5000, "status": "success"},
    {"name": "B", "type": "Cash", "amount": 8000, "status": "success"},
    {"name": "C", "type": "Online", "amount": 12000, "status": "failed"},
    {"name": "D", "type": "Card", "amount": 15000, "status": "success"},
    {"name": "E", "type": "Cash", "amount": 3000, "status": "success"}
]

blocked_types = ["Cash"]

total= sum(
    payment["amount"]
    for payment in payments
    if payment["type"] not in blocked_types
    and payment["status"] == "success"
    and payment["amount"] >= 5000
)

print(total)