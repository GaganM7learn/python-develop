students = {
    "s1": {"name": "Kiran", "age": 21, "course": "Go"},
    "s2": {"name": "Pooja", "age": 23, "course": "Python"},
    "s3": {"name": "Amit", "age": 20, "course": "Rust"},
    "s4": {"name": "Lina", "age": 25, "course": "Java"},
    "s5": {"name": "Raj", "age": 22, "course": "C++"}
}
preferred_courses = ["Go" , "Rust"]

for student_id , info in students.items():
    if not (info["course"] in preferred_courses) :
        print(info["name"])