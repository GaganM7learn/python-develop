students = {
    "s1": {"name": "Rahul", "age": 21, "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "course": "Java"},
    "s3": {"name": "Arjun", "age": 23, "course": "C++"},
    "s4": {"name": "Pooja", "age": 19, "course": "Python"},
    "s5": {"name": "Kiran", "age": 26, "course": "Java"}
}

selected_students = []

for student_id , info in students.items():
    if (20 <= info['age'] <= 25 and not info["age"] < 22 ) or info["course"] == "Python" :
        selected_students.append(info["name"])

print(selected_students)