students = {
    "s1": {"name": "Arun", "age": 22, "course": "Python"},
    "s2": {"name": "Maya", "age": 20, "course": "Java"},
    "s3": {"name": "Dev", "age": 24, "course": "C++"},
    "s4": {"name": "Sara", "age": 19, "course": "Rust"}
}
preferred_courses = ["Python" , "Java"]
for student_id , info in students.items():
    if not (info["course"] in preferred_courses ) :
        print(info["course"])