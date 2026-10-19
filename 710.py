staff = [
    {"name": "Ana", "dept": "IT", "sales": 70000, "bonus": 5000},
    {"name": "Ben", "dept": "Support", "sales": 80000, "bonus": 4000},
    {"name": "Cal", "dept": "Sales", "sales": 45000, "bonus": 3000},
    {"name": "Dee", "dept": "IT", "sales": 25000, "bonus": 2000}
]

blocked = ["Support"]

total = sum(
    s["bonus"]
    for s in staff
    if s["dept"] not in blocked
    and (s["dept"] == "IT" or s["sales"] >= 60000)
    and not (s["dept"] == "IT" and s["sales"] < 30000)
)

print(total)