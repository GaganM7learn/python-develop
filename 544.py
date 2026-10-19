students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 19, "course": "Java"},
    "s3": {"name": "Arjun", "age": 24, "course": "C++"},
    "s4": {"name": "Pooja", "age": 17, "course": "Rust"},
    "s5": {"name": "Kiran", "age": 26, "course": "Go"}
}

target_courses = ["Java" , "Python"]

for student_id , info in students.items():
    if info["course"] in target_courses or info['age'] >= 25 :
        print(info["name"])