refunds = [
    {"type": "Product", "amount": 12000, "fee": 500, "status": "approved"},
    {"type": "Delivery", "amount": 8000, "fee": 300, "status": "approved"},
    {"type": "Service", "amount": 30000, "fee": 1500, "status": "approved"},
    {"type": "Product", "amount": 9000, "fee": 400, "status": "pending"}
]

blocked = ["Delivery"]

total = sum(
    r["amount"] - r["fee"]
    for r in refunds
    if r["type"] not in blocked
    and r["status"] == "approved"
    and (r["type"] == "Product" or r["amount"] >= 25000)
)

print(total)  # 40000