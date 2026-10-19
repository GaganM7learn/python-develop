refunds = [
    {"name": "R1", "type": "Product", "amount": 22000, "status": "approved"},
    {"name": "R2", "type": "Service", "amount": 14000, "status": "approved"},
    {"name": "R3", "type": "Delivery", "amount": 32000, "status": "approved"},
    {"name": "R4", "type": "Product", "amount": 11000, "status": "approved"},
    {"name": "R5", "type": "Service", "amount": 28000, "status": "pending"},
    {"name": "R6", "type": "Product", "amount": 17000, "status": "approved"},
    {"name": "R7", "type": "Delivery", "amount": 36000, "status": "approved"}
]

blocked_types = ["Delivery"]

total_refunds = sum(
    exp["amount"]
    for exp in refunds
    if exp["type"] not in blocked_types
    and exp["status"] == "approved"
    and (
        exp["type"] == "Product"
        or exp["amount"] >= 25000
    )
    and not (
        exp["type"] == "Product"
        and exp["amount"] < 15000
    )
)
print(total_refunds)