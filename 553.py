students = {
    "s1": {"name": "Naveen", "age": 21, "course": "Go"},
    "s2": {"name": "Riya", "age": 18, "course": "Java"},
    "s3": {"name": "Manoj", "age": 26, "course": "Rust"},
    "s4": {"name": "Simran", "age": 23, "course": "Python"},
    "s5": {"name": "Ajay", "age": 17, "course": "C++"}
}

allowed_courses = ["Go" , "Rust"]

for student_id , info in students.items():
    if not(info["course"] in allowed_courses) and info['age'] >= 20:
        print(info["name"])