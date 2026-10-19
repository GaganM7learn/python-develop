students = {
    "s1": {"name": "Neha", "age": 22, "course": "Java"},
    "s2": {"name": "Amit", "age": 24, "course": "SQL"},
    "s3": {"name": "Sneha", "age": 20, "course": "Python"},
    "s4": {"name": "Varun", "age": 25, "course": "C++"},
    "s5": {"name": "Priti", "age": 27, "course": "JavaScript"},
    "s6": {"name": "Ravi", "age": 23, "course": "HTML"}
}

selected_students = []
for student_id , info in students.items():
    if 20 <= info["age"] <= 25 and not (info["course"] == "Java" or info["course"] == "Python") :
        selected_students.append(info["name"])

print(selected_students)