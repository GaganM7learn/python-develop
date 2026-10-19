claims = [
    {"name": "Claim P", "type": "Property", "amount": 50000, "deductible": 5000, "status": "approved"},
    {"name": "Claim Q", "type": "Medical", "amount": 22000, "deductible": 2000, "status": "approved"},
    {"name": "Claim R", "type": "Travel", "amount": 35000, "deductible": 3000, "status": "approved"},
    {"name": "Claim S", "type": "Property", "amount": 28000, "deductible": 4000, "status": "pending"},
    {"name": "Claim T", "type": "Vehicle", "amount": 40000, "deductible": 6000, "status": "approved"},
    {"name": "Claim U", "type": "Medical", "amount": 18000, "deductible": 1500, "status": "approved"}
]

blocked_types = ["Travel"]

total_claim = sum(
    claim['amount'] - claim["deductible"]
    for claim in claims
    if claim["type"] not in blocked_types
    and claim["status"] == "approved"
    and (
        claim["type"] == 'Medical' or claim['amount'] >= 35000
    )
)

print(total_claim)