expenses = [
    {"name": "E1", "department": "Engineering", "amount": 17000, "status": "approved"},
    {"name": "E2", "department": "Design", "amount": 24000, "status": "approved"},
    {"name": "E3", "department": "Support", "amount": 30000, "status": "approved"},
    {"name": "E4", "department": "Engineering", "amount": 11000, "status": "approved"},
    {"name": "E5", "department": "Marketing", "amount": 21000, "status": "pending"},
    {"name": "E6", "department": "Marketing", "amount": 26000, "status": "approved"},
    {"name": "E7", "department": "Engineering", "amount": 14000, "status": "approved"}
]

blocked_departments = ["Support"]
total_amount = sum(
    exp["amount"]
    for exp in expenses
    if exp["department"] not in blocked_departments
    and exp["status"] == "approved"
    and (
        exp["department"] == "Engineering" 
        or exp['amount'] >= 20000
    )
    and not ( 
        exp['department'] == "Engineering"
        and exp["amount"] < 15000
    )
    )

print(total_amount)