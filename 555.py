students = {
    "s1": {"name": "Varun", "age": 20, "course": "Go"},
    "s2": {"name": "Isha", "age": 16, "course": "Python"},
    "s3": {"name": "Rohan", "age": 24, "course": "Rust"},
    "s4": {"name": "Deepa", "age": 19, "course": "Java"},
    "s5": {"name": "Maya", "age": 21, "course": "C++"}
}
allowed_courses = ["Go", "Rust"]

for student_id , info in students.items():
    if not (info["course"] in allowed_courses) or info["age"] < 18 :
        print(info["name"])