workers = [
    {"name": "Kiran", "department": "Engineering", "sales": 75000, "bonus_rate": 0.12, "status": "active"},
    {"name": "Pooja", "department": "Marketing", "sales": 55000, "bonus_rate": 0.06, "status": "active"},
    {"name": "Arjun", "department": "Support", "sales": 85000, "bonus_rate": 0.07, "status": "active"},
    {"name": "Meera", "department": "Engineering", "sales": 40000, "bonus_rate": 0.12, "status": "inactive"},
    {"name": "Vikram", "department": "Marketing", "sales": 70000, "bonus_rate": 0.06, "status": "active"},
    {"name": "Sara", "department": "Support", "sales": 45000, "bonus_rate": 0.07, "status": "active"}
]

blocked_departments = ["Support"]

total_bonus = sum(
    worker["sales"] * worker["bonus_rate"]
    for worker in workers
    if worker["department"] not in blocked_departments
    and (
        worker["department"] == "Engineering" or worker["sales"]>= 65000


    )
    and worker["status"] == "active"
)

print(total_bonus)