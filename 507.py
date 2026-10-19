students = {
    "s1": {"name": "Aarav", "age": 21, "course": "Python"},
    "s2": {"name": "Maya", "age": 23, "course": "Java"},
    "s3": {"name": "Ravi", "age": 26, "course": "Python"},
    "s4": {"name": "Sneha", "age": 24, "course": "Python"},
    "s5": {"name": "Kiran", "age": 19, "course": "Python"}
}
selected_students = []
for student_id , info in students.items():
    if 20 <= info["age"] <= 25 and info["course"] == "Python" :
        selected_students.append(info["name"])

print(selected_students)