students = {
    "s1": {"name": "Kavya", "age": 21, "course": "Go"},
    "s2": {"name": "Rohan", "age": 23, "course": "Python"},
    "s3": {"name": "Isha", "age": 20, "course": "Java"},
    "s4": {"name": "Manoj", "age": 18, "course": "C++"},
    "s5": {"name": "Sara", "age": 25, "course": "Rust"}
}

preferred_courses = ["Go", "C++"]

blocked_courses = ["Java" , "Rust"]

for student_id , info in students.items():
    if info["course"] in preferred_courses or info["course"] not in blocked_courses :
        print(info["name"])