students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "course": "Java"},
    "s3": {"name": "Arjun", "age": 19, "course": "C++"},
    "s4": {"name": "Pooja", "age": 21, "course": "Rust"},
    "s5": {"name": "Kiran", "age": 17, "course": "Go"}
}
preferred_courses = ["Python" , "C++" , "Rust"]
blocked_courses = ["Java" , "Go"]

for student_id , info in students.items():
    if info["course"] in preferred_courses and info["course"] not in blocked_courses :
        print(info["name"])