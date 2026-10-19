students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 17, "course": "Java"},
    "s3": {"name": "Arjun", "age": 25, "course": "C++"},
    "s4": {"name": "Pooja", "age": 21, "course": "Rust"},
    "s5": {"name": "Kiran", "age": 16, "course": "Go"}
}

technical_courses = ["Python" , "Rust"]
for student_id , info in students.items():
    if (info["course"] in technical_courese and info["age"] >= 20 ) or info["age"] < 18 :
        print(info["name"])