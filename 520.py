students = {
    "s1": {"name": "Asha", "age": 22, "course": "Java"},
    "s2": {"name": "Ravi", "age": 25, "course": "SQL"},
    "s3": {"name": "Nisha", "age": 21, "course": "Python"},
    "s4": {"name": "Karan", "age": 24, "course": "C++"},
    "s5": {"name": "Divya", "age": 26, "course": "HTML"},
    "s6": {"name": "Mohan", "age": 20, "course": "JavaScript"}
}

selected_students = []

allowed_course = ["Python" , "Java" , "SQL"]

for student_id , info in students.items():
    if 20 <= info["age"] <= 25 and info["course"] in allowed_course :

        selected_students.append(info["name"])

print(selected_students)