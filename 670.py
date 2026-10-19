payments = [
    {"name": "A", "method": "Card", "amount": 12000, "status": "successful"},
    {"name": "B", "method": "Cash", "amount": 8000, "status": "successful"},
    {"name": "C", "method": "UPI", "amount": 15000, "status": "successful"},
    {"name": "D", "method": "Card", "amount": 6000, "status": "pending"},
    {"name": "E", "method": "Bank", "amount": 20000, "status": "successful"}
]

blocked_methods = ["Cash", "Bank"]

total_amount = sum(
    payment["amount"]
    for payment in payments
    if payment['method'] not in blocked_methods
    and payment["status"] == "successful"
    and(
        payment["method"] == "Card"
        or payment['amount'] >= 10000
    )
)

print(total_amount)