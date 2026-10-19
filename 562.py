students = {
    "s1": {"name": "Asha", "age": 22, "course": "Go"},
    "s2": {"name": "Vikram", "age": 16, "course": "Java"},
    "s3": {"name": "Nisha", "age": 24, "course": "Rust"},
    "s4": {"name": "Karan", "age": 21, "course": "Python"},
    "s5": {"name": "Divya", "age": 17, "course": "C++"}
}

preferred_courses = ["Go", "Rust", "C++"]
blocked_courses = ["Java", "Python"]
for student_id , info in students.items():
    if (info["course"] in preferred_courses and info["course"] not in blocked_courses) or info["age"] < 18 :
        print(info["name"])