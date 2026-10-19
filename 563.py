students = {
    "s1": {"name": "Arun", "age": 22, "course": "Python"},
    "s2": {"name": "Maya", "age": 17, "course": "Java"},
    "s3": {"name": "Dev", "age": 25, "course": "C++"},
    "s4": {"name": "Sara", "age": 19, "course": "Rust"}
}

allowed_courses = ["Python", "C++"]
for student_id , info in students.items():
    if info["course"] in allowed_courses and info["age"] >= 20 or info['age'] < 18 :
        print(info["name"])