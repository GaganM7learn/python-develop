payments = [
    {"id": 101, "method": "Card", "amount": 18000, "status": "success"},
    {"id": 102, "method": "Cash", "amount": 25000, "status": "success"},
    {"id": 103, "method": "UPI", "amount": 9000, "status": "success"},
    {"id": 104, "method": "Card", "amount": 22000, "status": "pending"},
    {"id": 105, "method": "UPI", "amount": 16000, "status": "success"},
    {"id": 106, "method": "Cash", "amount": 14000, "status": "success"}
]

blocked_methods = ["Cash"]

total = sum(
    pay['amount']
    for pay in payments
    if pay["method"] not in blocked_methods
    and pay["status"] == "success"
    and (
        pay["method"] == "Card" 
        or pay['amount'] >= 15000
    )
    and not (
        pay["method"] == "Card"
        and pay["amount"] < 15000
    )
)
print(total)