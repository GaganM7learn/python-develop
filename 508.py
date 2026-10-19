students = {
    "s1": {"name": "Varsha", "age": 22, "course": "Java"},
    "s2": {"name": "Akash", "age": 24, "course": "C++"},
    "s3": {"name": "Leena", "age": 21, "course": "Java"},
    "s4": {"name": "Rohit", "age": 26, "course": "Java"},
    "s5": {"name": "Pavan", "age": 19, "course": "Java"},
    "s6": {"name": "Sonal", "age": 23, "course": "Python"}
}

selected_students = []

for student_id ,info in students.items():
    if 20 <= info["age"]  <= 25 and info["course"] == "Java" :
        selected_students.append(info["name"])

print(selected_students)