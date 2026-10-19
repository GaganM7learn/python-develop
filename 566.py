students = {
    "s1": {"name": "Vijay", "age": 22, "course": "Go"},
    "s2": {"name": "Sneha", "age": 17, "course": "Java"},
    "s3": {"name": "Amit", "age": 19, "course": "Rust"},
    "s4": {"name": "Kavya", "age": 25, "course": "Python"},
    "s5": {"name": "Ravi", "age": 16, "course": "C++"}
}

allowed_courses = ["Go", "Rust", "C++"]
for student_id , info in students.items():
    if info["course"] in allowed_courses and ( info["age"] >= 20 or info["age"] < 18):
        print(info["name"])