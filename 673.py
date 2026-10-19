staff = [
    {"name": "Kiran", "department": "Engineering", "salary": 75000, "status": "active"},
    {"name": "Pooja", "department": "Support", "salary": 42000, "status": "active"},
    {"name": "Dev", "department": "Engineering", "salary": 38000, "status": "active"},
    {"name": "Sara", "department": "Marketing", "salary": 55000, "status": "active"},
    {"name": "Amit", "department": "Finance", "salary": 80000, "status": "active"},
    {"name": "Isha", "department": "Marketing", "salary": 35000, "status": "inactive"},
    {"name": "Vikram", "department": "Engineering", "salary": 46000, "status": "active"}
]

excluded_departments = ["Support", "Finance"]

total_salary = sum(
    ids['salary']
    for ids in staff
    if ids["department"] not in excluded_departments
    and ids['status'] == "active"
    and not (
        ids["department"] == "Engineering"
        and ids["salary"] < 45000
    )
)

print(total_salary)