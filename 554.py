students = {
    "s1": {"name": "Aman", "age": 22, "course": "Python"},
    "s2": {"name": "Riya", "age": 17, "course": "Java"},
    "s3": {"name": "Karan", "age": 25, "course": "C++"},
    "s4": {"name": "Neha", "age": 19, "course": "Rust"}
}
allowed_courses = ["Python", "C++"]

for student_id , info in students.items():
    if not (info["course"] in allowed_courses ) or info["age"] < 18 :
        print(info["name"])