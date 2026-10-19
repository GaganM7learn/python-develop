employees = [
    {"name": "Asha", "dept": "Engineering", "sales": 70000, "bonus": 5000, "status": "active"},
    {"name": "Ravi", "dept": "Support", "sales": 80000, "bonus": 4000, "status": "active"},
    {"name": "Maya", "dept": "Sales", "sales": 45000, "bonus": 3000, "status": "active"},
    {"name": "Dev", "dept": "Engineering", "sales": 30000, "bonus": 2500, "status": "inactive"}
]

blocked_depts = ["Support"]

total_bonus = sum(
    e["bonus"]
    for e in employees
    if e["dept"] not in blocked_depts
    and e["status"] == "active"
    and (
        e["dept"] == "Engineering"
        or e["sales"] >= 60000
    )
    and not (
        e["dept"] == "Engineering"
        and e["sales"] < 40000
    )
)

print(total_bonus)