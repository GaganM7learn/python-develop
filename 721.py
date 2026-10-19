refunds = [
    {"type": "Product", "amount": 18000, "fee": 800, "status": "approved"},
    {"type": "Delivery", "amount": 25000, "fee": 1000, "status": "approved"},
    {"type": "Service", "amount": 22000, "fee": 1200, "status": "approved"},
    {"type": "Product", "amount": 8000, "fee": 300, "status": "approved"},
    {"type": "Product", "amount": 30000, "fee": 1500, "status": "pending"}
]
blocked = ["Delivery"]

total = sum(
    p['amount'] - p["fee"]
    for p in refunds
    if p["type"] not in blocked
    and p['status'] == "approved"
    and (p["type"] == "Product" or p["amount"] >= 20000 )
    and not ( p["type"] == "Product" and p["amount"] < 10000 ) 
)

print(total)