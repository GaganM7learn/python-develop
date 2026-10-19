students = {
    "s1": {"name": "Rahul", "age": 23, "course": "Python"},
    "s2": {"name": "Ananya", "age": 25, "course": "Java"},
    "s3": {"name": "Vijay", "age": 24, "course": "C++"},
    "s4": {"name": "Pooja", "age": 21, "course": "Python"},
    "s5": {"name": "Karthik", "age": 26, "course": "JavaScript"}
}

selected_students = []

for student_id , info in students.items():
    if 22 <= info['age'] <= 26 and not info["course"] == "Java" :
        selected_students.append(info["name"])


print(selected_students)