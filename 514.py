students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "course": "C++"},
    "s3": {"name": "Arjun", "age": 21, "course": "JavaScript"},
    "s4": {"name": "Priya", "age": 26, "course": "Java"},
    "s5": {"name": "Kiran", "age": 23, "course": "SQL"}
}

selected_students = []

for student_id , info in students.items():
    if 20 <= info['age'] < 25 and not (info["course"] == "Python" or info["course"] == "Java") :
        selected_students.append(info["name"])

print(selected_students)