claims = [
    {"name": "C1", "type": "Medical", "amount": 25000, "status": "approved"},
    {"name": "C2", "type": "Travel", "amount": 18000, "status": "approved"},
    {"name": "C3", "type": "Vehicle", "amount": 40000, "status": "approved"},
    {"name": "C4", "type": "Medical", "amount": 12000, "status": "pending"},
    {"name": "C5", "type": "Property", "amount": 35000, "status": "approved"},
    {"name": "C6", "type": "Medical", "amount": 16000, "status": "approved"}
]

blocked_types = ["Travel"]

total_claims = sum(
    claim["amount"]
    for claim in claims
    if claim["type"] not in blocked_types
    and claim["status"] == "approved"
    and (
        claim["type"] == "Medical"
        or claim["amount"] >= 30000
    )
    and not (
        claim["type"] == "Medical"
        and claim["amount"] < 15000
    )
)

print(total_claims)