students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 19, "course": "Java"},
    "s3": {"name": "Arjun", "age": 24, "course": "C++"},
    "s4": {"name": "Pooja", "age": 17, "course": "Rust"}
}

allowed_courses = ["Python" , "Java"]

for student_id , info in students.items():
    if not(info["course"] in allowed_courses) and info["age"]:
        print(info["name"])