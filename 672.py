employees = [
    {"name": "Asha", "department": "IT", "salary": 60000, "status": "active"},
    {"name": "Ravi", "department": "HR", "salary": 45000, "status": "active"},
    {"name": "Maya", "department": "Sales", "salary": 52000, "status": "inactive"},
    {"name": "John", "department": "IT", "salary": 40000, "status": "active"},
    {"name": "Neha", "department": "Finance", "salary": 70000, "status": "active"}
]

excluded_departments = ["HR", "Finance"]

total_salary = sum(
    employeess["salary"]
    for employeess in employees
    if employeess['department'] not in excluded_departments
    and employeess["status"] == "active"
    and not (
        employeess["department"] == "IT"
        and employeess['salary'] < 50000
    )
)

print(total_salary)