students = {
    "s1": {"name": "Arun", "age": 18, "course": "Python"},
    "s2": {"name": "Meena", "age": 22, "course": "Java"},
    "s3": {"name": "Ravi", "age": 25, "course": "C++"},
    "s4": {"name": "Pooja", "age": 30, "course": "Python"},
    "s5": {"name": "Kiran", "age": 24, "course": "Java"}
}

selected_students = []

for student_id , info in students.items():
    if 20 <= info["age"] <= 25 :
        selected_students.append(info["name"])

print(selected_students)