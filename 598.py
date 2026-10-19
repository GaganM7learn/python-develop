employees = [
    {"name": "Zara", "department": "HR"},
    {"name": "Amit", "department": "IT"},
    {"name": "Riya", "department": "Finance"},
    {"name": "Kabir", "department": "Sales"}
]

sorted_employee = sorted(employees , key=lambda item : item["name"])

print(sorted_employee)