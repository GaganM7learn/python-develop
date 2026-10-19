students = {
    "s1": {"name": "Aman", "age": 22, "course": "Python"},
    "s2": {"name": "Riya", "age": 17, "course": "Java"},
    "s3": {"name": "Karan", "age": 19, "course": "C++"},
    "s4": {"name": "Tina", "age": 25, "course": "Rust"}
}

allowed_courses = ["Python", "C++"]
for student_id , info in students.items():
    if info["course"] in allowed_courses and info["age"] >= 20 or info["age"] < 18 :
        print(info["name"])