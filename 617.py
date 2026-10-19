employees = [
    {"name": "Arjun", "department": "IT", "salary": 65000, "experience": 3},
    {"name": "Meera", "department": "HR", "salary": 72000, "experience": 5},
    {"name": "Vikram", "department": "IT", "salary": 85000, "experience": 7},
    {"name": "Nisha", "department": "Finance", "salary": 78000, "experience": 6},
    {"name": "Rahul", "department": "IT", "salary": 55000, "experience": 2}
]

highest_it_paid_employee = max(( employee for employee in employees if employee ["department"] == "IT" and employee["experience"] > 2 ) , key=lambda emploee : emploee["salary"] )
print(highest_it_paid_employee)