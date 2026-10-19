refunds = [
    {"type": "Product", "amount": 18000, "fee": 1000, "status": "approved"},
    {"type": "Delivery", "amount": 9000, "fee": 500, "status": "approved"},
    {"type": "Product", "amount": 12000, "fee": 700, "status": "approved"},
    {"type": "Service", "amount": 30000, "fee": 2000, "status": "approved"}
]

blocked_types = ["Delivery"]

total = sum(
    r["amount"] - r["fee"]
    for r in refunds
    if r["type"] not in blocked_types
    and r["status"] == "approved"
    and (
        r["type"] == "Product"
        or r["amount"] >= 25000
    )
    and not (
        r["type"] == "Product"
        and r["amount"] < 15000
    )
)

print(total)