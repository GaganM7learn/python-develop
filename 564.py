students = {
    "s1": {"name": "Nitin", "age": 23, "course": "Go"},
    "s2": {"name": "Priya", "age": 18, "course": "Java"},
    "s3": {"name": "Mohan", "age": 26, "course": "Rust"},
    "s4": {"name": "Anu", "age": 16, "course": "Python"},
    "s5": {"name": "Raj", "age": 21, "course": "C++"}
}

allowed_courses = ["Go", "Rust", "C++"]

for student_id , info in students.items():
    if info["course"] in allowed_courses and info["age"] >= 21 or info["age"] < 18 :
        print(info["name"])