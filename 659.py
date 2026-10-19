claims = [
    {"name": "Claim A", "type": "Health", "amount": 25000, "deductible": 2000, "status": "approved"},
    {"name": "Claim B", "type": "Vehicle", "amount": 40000, "deductible": 5000, "status": "approved"},
    {"name": "Claim C", "type": "Travel", "amount": 12000, "deductible": 1000, "status": "rejected"},
    {"name": "Claim D", "type": "Health", "amount": 18000, "deductible": 1500, "status": "approved"},
    {"name": "Claim E", "type": "Vehicle", "amount": 30000, "deductible": 3000, "status": "approved"}
]

blocked_types = ["Travel"]

total_payout = sum(
    claim['amount'] - claim["deductible"]
    for claim in claims
    if claim["type"] not in blocked_types
    and (
        claim["type"] == "Health"
        or claim['amount'] >= 30000
    )
)

print(total_payout)