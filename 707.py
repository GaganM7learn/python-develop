workers = [
    {"name": "Nina", "dept": "Engineering", "salary": 62000, "status": "active"},
    {"name": "Omar", "dept": "Support", "salary": 40000, "status": "active"},
    {"name": "Liam", "dept": "Sales", "salary": 57000, "status": "active"},
    {"name": "Mia", "dept": "Engineering", "salary": 45000, "status": "inactive"},
    {"name": "Noah", "dept": "Finance", "salary": 53000, "status": "active"}
]

blocked_depts = ["Support"]

total = sum(
    p["salary"]
    for p in workers
    if p["dept"] not in blocked_depts
    and p["status"] == "active"
    and ( p["dept"] == "Engineering"
         or p["salary"] >= 55000)
)

print(total)