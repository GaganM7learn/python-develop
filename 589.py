students = [
    {"name": "Asha", "age": 22},
    {"name": "Ravi", "age": 19},
    {"name": "Kiran", "age": 25},
    {"name": "Meera", "age": 21}
]

sorted_students = sorted(students , key=lambda studen : studen["age"])

print(sorted_students)