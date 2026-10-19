students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 17, "course": "Java"},
    "s3": {"name": "Arjun", "age": 25, "course": "C++"},
    "s4": {"name": "Pooja", "age": 20, "course": "Rust"},
    "s5": {"name": "Kiran", "age": 16, "course": "Go"}
}

blocked_courses = ["Java" , "C++"]

for student_id , info in students.items():
    if (info["course"] not in blocked_courses and info["age"] >= 20) or info["age"] < 18 :
        print(info["name"])