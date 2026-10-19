students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 17, "course": "Java"},
    "s3": {"name": "Arjun", "age": 25, "course": "C++"},
    "s4": {"name": "Pooja", "age": 19, "course": "Rust"},
    "s5": {"name": "Kiran", "age": 26, "course": "Go"}
}

technical_courses = ["Python", "C++", "Rust"]
other_courses = ["Go", "Java"]
for student_id , info in students.items():
    if (( info["course"] in technical_courses and info["age"] >= 20) or (info["course"] in other_courses and info["age"] < 20)):
        print(info["name"])