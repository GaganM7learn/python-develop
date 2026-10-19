refunds = [
    {"type": "Product", "amount": 20000, "fee": 1000, "status": "approved"},
    {"type": "Delivery", "amount": 12000, "fee": 500, "status": "approved"},
    {"type": "Service", "amount": 30000, "fee": 2000, "status": "approved"},
    {"type": "Product", "amount": 10000, "fee": 500, "status": "approved"}
]

blocked = ["Delivery"]

total = sum(
    r["amount"] - r["fee"]
    for r in refunds
    if r["type"] not in blocked
    and r["status"] == "approved"
    and (r["type"] == "Product" or r["amount"] >= 25000)
    and not (r["type"] == "Product" and r["amount"] < 15000)
)

print(total)

refunds = [
    {"type": "Product", "amount": 20000, "fee": 1000, "status": "approved"},
    {"type": "Delivery", "amount": 12000, "fee": 500, "status": "approved"},
    {"type": "Service", "amount": 30000, "fee": 2000, "status": "approved"},
    {"type": "Product", "amount": 10000, "fee": 500, "status": "approved"}
]

blocked = ["Delivery"]

total = sum(
    r["amount"] - r["fee"]
    for r in refunds
    if r["type"] not in blocked
    and r["status"] == "approved"
    and (r["type"] == "Product" or r["amount"] >= 25000)
    and not (r["type"] == "Product" and r["amount"] < 15000)
)

print(total)