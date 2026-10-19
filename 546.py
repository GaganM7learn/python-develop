students = {
    "s1": {"name": "Ravi", "age": 22, "course": "Python"},
    "s2": {"name": "Anu", "age": 19, "course": "Java"},
    "s3": {"name": "Karan", "age": 25, "course": "C++"},
    "s4": {"name": "Tina", "age": 17, "course": "Rust"}
}

blocked_courses = ["Java", "C++"]

for student_id , info in students.items():
    if info["course"] not in blocked_courses or info['age'] < 18 :
        print(info["name"])