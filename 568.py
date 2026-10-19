students = {
    "s1": {"name": "Asha", "age": 23, "course": "Go"},
    "s2": {"name": "Rohan", "age": 18, "course": "Python"},
    "s3": {"name": "Divya", "age": 16, "course": "Java"},
    "s4": {"name": "Manish", "age": 24, "course": "Rust"},
    "s5": {"name": "Kavya", "age": 19, "course": "C++"},
    "s6": {"name": "Arun", "age": 17, "course": "JavaScript"}
}

technical_courses = ["Go", "Rust", "C++"]
other_courses = ["Java", "JavaScript", "Python"]

for student_id , info in students.items():
    if ((info["course"] in technical_courses and info["age"] >= 21) or ( info["course"] in other_courses and info['age'] < 18 )):
        print(info["name"])