students = [
    {"name": "Asha", "course": "Python", "age": 22},
    {"name": "Ravi", "course": "Java", "age": 20},
    {"name": "Meera", "course": "Python", "age": 19},
    {"name": "Kiran", "course": "Java", "age": 24}
]

sorted_students = sorted( students , key=lambda student : (student["course"] , student["age"]))
print(sorted_students)