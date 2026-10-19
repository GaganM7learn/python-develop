staff = [
    {"name": "Ava", "dept": "IT", "sales": 70000, "bonus": 5000},
    {"name": "Ben", "dept": "HR", "sales": 45000, "bonus": 2000},
    {"name": "Cal", "dept": "Sales", "sales": 85000, "bonus": 6000},
    {"name": "Dee", "dept": "IT", "sales": 25000, "bonus": 1500}
]

blocked = ["HR"]

total = sum(
    s["bonus"]
    for s in staff
    if s["dept"] not in blocked
    and (s["dept"] == "IT" or s["sales"] >= 80000)
    and not (s["dept"] == "IT" and s["sales"] < 30000)
)

print(total)  # 11000