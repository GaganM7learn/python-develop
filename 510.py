students = {
    "s1": {"name": "Nisha", "age": 22, "course": "Java"},
    "s2": {"name": "Dev", "age": 25, "course": "Python"},
    "s3": {"name": "Isha", "age": 19, "course": "Java"},
    "s4": {"name": "Manoj", "age": 24, "course": "C++"},
    "s5": {"name": "Tara", "age": 21, "course": "Python"},
    "s6": {"name": "Vikram", "age": 26, "course": "Java"}
}

selected_students = []

for student_id , info in students.items():
    if 21 <= info["age"] <= 25 and (info["course"] == "Python" or info["course"] == "Java"):
        selected_students.append(info["name"])


print(selected_students)