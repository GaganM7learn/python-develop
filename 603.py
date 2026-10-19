employees = [
    {"name": "Anita", "department": "Sales", "salary": 52000},
    {"name": "Rahul", "department": "IT", "salary": 78000},
    {"name": "Kavya", "department": "Sales", "salary": 65000},
    {"name": "Mohan", "department": "IT", "salary": 62000}
]

sorted_employees = sorted( employees , key=lambda employe : ( employe["department"] , employe["salary"]) , reverse=True)

print(sorted_employees)