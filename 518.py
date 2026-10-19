students = {
    "s1": {"name": "Isha", "age": 22, "course": "Java"},
    "s2": {"name": "Varun", "age": 24, "course": "Python"},
    "s3": {"name": "Nikhil", "age": 17, "course": "SQL"},
    "s4": {"name": "Pooja", "age": 20, "course": "C++"},
    "s5": {"name": "Aditya", "age": 26, "course": "JavaScript"},
    "s6": {"name": "Simran", "age": 19, "course": "Java"}
}

selected_students = []
for student_id , info in students.items():
    if (21 <= info['age'] <= 25 and info["course"] == "Java") or ( not info['age'] < 18 and not info['course'] == "Python") :
        selected_students.append(info["name"])


print(selected_students)