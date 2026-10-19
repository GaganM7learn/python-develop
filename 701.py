staff = [
    {"name": "Nina", "dept": "Engineering", "sales": 55000, "bonus": 4500, "status": "active"},
    {"name": "Omar", "dept": "Support", "sales": 90000, "bonus": 5000, "status": "active"},
    {"name": "Liam", "dept": "Sales", "sales": 65000, "bonus": 3500, "status": "active"},
    {"name": "Mia", "dept": "Engineering", "sales": 30000, "bonus": 2500, "status": "active"},
    {"name": "Noah", "dept": "Finance", "sales": 70000, "bonus": 4000, "status": "inactive"}
]

blocked_depts = ["Support"]

total = sum(
    p["bonus"]
    for p in staff
    if p["dept"] not in blocked_depts
    and p['status'] == "active"
    and ( p['dept'] == "Engineering" or p["sales"] >= 60000)
    and not ( p["dept"] == "Engineering"
             and p["sales"] < 40000)
)

print(total)