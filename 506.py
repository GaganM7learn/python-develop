students = {
    "s1": {"name": "Gaurav", "age": 17, "course": "Python"},
    "s2": {"name": "Nisha", "age": 20, "course": "Java"},
    "s3": {"name": "Rohan", "age": 23, "course": "C++"},
    "s4": {"name": "Kavita", "age": 27, "course": "Python"},
    "s5": {"name": "Manoj", "age": 25, "course": "Java"},
    "s6": {"name": "Suresh", "age": 29, "course": "C++"}
}

selected_students = []

for student_id , info in students.items():
    if 20 <= info["age"] <= 25 :
        selected_students.append(info["name"])

print(selected_students)