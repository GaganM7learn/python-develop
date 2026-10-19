employees = [
    {"name": "Asha", "dept": "IT", "salary": 50000, "status": "active"},
    {"name": "Ravi", "dept": "HR", "salary": 35000, "status": "active"},
    {"name": "Maya", "dept": "IT", "salary": 42000, "status": "inactive"},
    {"name": "Dev", "dept": "Sales", "salary": 60000, "status": "active"}
]

blocked_depts = ["HR"]

total = sum(
    e["salary"]
    for e in employees
    if e["dept"] not in blocked_depts
    and e["status"] == "active"
    and (e["dept"] == "IT" or e["salary"] >= 55000)
)

print(total)