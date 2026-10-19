claims = [
    {"type": "Product", "amount": 22000, "fee": 1200, "status": "approved"},
    {"type": "Delivery", "amount": 18000, "fee": 800, "status": "approved"},
    {"type": "Product", "amount": 12000, "fee": 500, "status": "approved"},
    {"type": "Service", "amount": 32000, "fee": 2000, "status": "approved"},
    {"type": "Product", "amount": 28000, "fee": 1500, "status": "pending"}
]

blocked_types = ["Delivery"]

total = sum(
    p["amount"] - p["fee"]
    for p in claims
    if p["type"] not in blocked_types
    and p["status"] == "approved"
    and ( p["type"] == "Product" or p["amount"] >= 25000)
    and not ( p["type"] == "Product" and p["amount"] < 15000)
)

print(total)