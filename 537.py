students = {
    "s1": {"name": "Neha", "age": 20, "course": "Java"},
    "s2": {"name": "Vikram", "age": 17, "course": "Python"},
    "s3": {"name": "Sneha", "age": 23, "course": "Python"},
    "s4": {"name": "Ravi", "age": 16, "course": "C++"},
    "s5": {"name": "Anita", "age": 26, "course": "Java"}
}

for student_id , info in students.items():
    if not info["course"] == "Java" or info ["age"] < 18 :

        print(info["name"])