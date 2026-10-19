employees = [
    {"name": "Neha", "salary": 55000},
    {"name": "Arjun", "salary": 72000},
    {"name": "Priya", "salary": 48000},
    {"name": "Vikram", "salary": 90000}
]

sorted_employees = sorted(employees , key=lambda row : row["salary"])

print(sorted_employees)