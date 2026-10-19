students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 19, "course": "Java"},
    "s3": {"name": "Arjun", "age": 24, "course": "C++"},
    "s4": {"name": "Pooja", "age": 17, "course": "Python"},
    "s5": {"name": "Kiran", "age": 26, "course": "Rust"}
}

allowed_courses = ["Python" , "C++" , "Rust"]

for student_id , info in students.items():
    if info["course"] in allowed_courses and info["age"] >= 20 :
        print(info["name"])