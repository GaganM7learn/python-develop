transactions = [
    {"name": "T1", "method": "Wallet", "amount": 7000, "status": "successful"},
    {"name": "T2", "method": "Card", "amount": 9000, "status": "successful"},
    {"name": "T3", "method": "Cash", "amount": 18000, "status": "successful"},
    {"name": "T4", "method": "UPI", "amount": 14000, "status": "successful"},
    {"name": "T5", "method": "Bank", "amount": 22000, "status": "successful"},
    {"name": "T6", "method": "Card", "amount": 5000, "status": "pending"},
    {"name": "T7", "method": "Wallet", "amount": 11000, "status": "successful"}
]

blocked_methods = ["Cash", "Bank"]

total_amount = sum(
    trans["amount"]
    for trans in transactions
    if trans["method"] not in blocked_methods
    and trans['status'] == "successful"
    and (
        trans["method"] == "Card"
        or trans["amount"] >= 10000
    )
)

print(total_amount)