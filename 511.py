students = {
    "s1": {"name": "Rahul", "age": 23, "course": "Python"},
    "s2": {"name": "Ananya", "age": 25, "course": "Java"},
    "s3": {"name": "Vijay", "age": 27, "course": "JavaScript"},
    "s4": {"name": "Pooja", "age": 24, "course": "Python"},
    "s5": {"name": "Karthik", "age": 22, "course": "JavaScript"},
    "s6": {"name": "Neha", "age": 26, "course": "Java"}
}

selected_students = []

for student_id , info in students.items():
    if 22 <= info["age"] <= 26 and ( info["course"] == "Java" or info["course"] == "Python") and not info["course"] == "JavaScript" :
        selected_students.append(info['name'])

print(selected_students)