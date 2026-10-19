students = {
    "s1": {"name": "Aarav", "age": 21, "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "course": "Java"},
    "s3": {"name": "Rohan", "age": 17, "course": "C++"},
    "s4": {"name": "Diya", "age": 23, "course": "SQL"},
    "s5": {"name": "Kabir", "age": 19, "course": "JavaScript"}
}

selected_students = []

for student_id , info in students.items():
    if ( 20 <= info['age'] <= 25 and info["course"] == "Python") or ( not info["age"] < 18 and not info['course'] == "Java"):
        selected_students.append(info["name"])

print(selected_students)