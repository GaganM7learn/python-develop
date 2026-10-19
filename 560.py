students = {
    "s1": {"name": "Aman", "age": 22, "course": "Python"},
    "s2": {"name": "Riya", "age": 19, "course": "Java"},
    "s3": {"name": "Karan", "age": 24, "course": "Rust"},
    "s4": {"name": "Tina", "age": 17, "course": "C++"},
    "s5": {"name": "Dev", "age": 26, "course": "Go"}
}
preferred_courses = ["Python" , "Rust"]

blocked_courses = ["Java"]

for student_id , info in students.items():
    if info["course"] in preferred_courses or info["course"] not in blocked_courses:
        print(info["name"])