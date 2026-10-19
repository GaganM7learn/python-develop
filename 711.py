team = [
    {"name": "Ira", "dept": "Engineering", "sales": 52000, "bonus": 4500},
    {"name": "Jay", "dept": "Support", "sales": 85000, "bonus": 5000},
    {"name": "Kim", "dept": "Sales", "sales": 68000, "bonus": 3500},
    {"name": "Leo", "dept": "Engineering", "sales": 25000, "bonus": 2200},
    {"name": "Uma", "dept": "Finance", "sales": 40000, "bonus": 3000}
]

blocked = ["Support"]

total = sum(
    p["bonus"]
    for p in team
    if p["dept"] not in blocked
    and ( p["dept"] == "Engineering" or p["sales"] >= 60000 )
    and not ( p["dept"] == "Engineering" and p["sales"] < 30000)
)

print(total)