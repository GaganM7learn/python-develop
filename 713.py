claims = [
    {"type": "Product", "amount": 24000, "fee": 1500, "status": "approved"},
    {"type": "Delivery", "amount": 18000, "fee": 700, "status": "approved"},
    {"type": "Service", "amount": 32000, "fee": 2000, "status": "approved"},
    {"type": "Product", "amount": 11000, "fee": 500, "status": "approved"},
    {"type": "Product", "amount": 28000, "fee": 1200, "status": "pending"}
]

blocked = ["Delivery"]

total = sum(
    r["amount"] * r["fee"]
    for r in claims
    if r["type"] not in blocked
    and r["status"] == "approved"
    and ( r["type"] == "Product" or r["amount"] >= 25000)
    and not ( r["type"] == "Product" and r["amount"] < 15000)
)

print(total)