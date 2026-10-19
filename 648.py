employees = [
    {"name": "Asha", "department": "IT", "sales": 80000, "bonus_rate": 0.10, "status": "active"},
    {"name": "Rahul", "department": "HR", "sales": 50000, "bonus_rate": 0.05, "status": "active"},
    {"name": "Maya", "department": "Sales", "sales": 90000, "bonus_rate": 0.08, "status": "inactive"},
    {"name": "Dev", "department": "IT", "sales": 40000, "bonus_rate": 0.10, "status": "active"},
    {"name": "Neha", "department": "Sales", "sales": 60000, "bonus_rate": 0.08, "status": "active"}
]

blocked_departments = ["HR"]

total_bonus = sum(
    employee["sales"] * employee["bonus_rate"]
    for employee in employees 
    if employee["department"] not in blocked_departments
    and (
        employee["department"] == "IT"
        or employee["sales"] >= 60000
    )
    and employee['status'] == "active"
)

print(total_bonus)