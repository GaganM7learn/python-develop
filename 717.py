staff = [
    {"name": "Maya", "dept": "IT", "sales": 50000, "bonus": 4000, "status": "active"},
    {"name": "Raj", "dept": "HR", "sales": 90000, "bonus": 5500, "status": "active"},
    {"name": "Zoe", "dept": "Sales", "sales": 65000, "bonus": 3500, "status": "active"},
    {"name": "Eli", "dept": "IT", "sales": 25000, "bonus": 1800, "status": "active"},
    {"name": "Noah", "dept": "IT", "sales": 70000, "bonus": 6000, "status": "inactive"}
]
blocked = ["HR"]

total = sum(
    p["bonus"]
    for p in staff
    if p["dept"] not in blocked
    and p["status"] == "active"
    and (p["dept"] == "IT" or p["sales"] >= 60000 )
    and not ( p["dept"] == "IT" and p["sales"] < 35000)
)
print(total)