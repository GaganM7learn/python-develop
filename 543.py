students = {
    "s1": {"name": "Neha", "age": 18, "course": "Java"},
    "s2": {"name": "Vikram", "age": 21, "course": "Go"},
    "s3": {"name": "Sneha", "age": 25, "course": "Python"},
    "s4": {"name": "Ravi", "age": 23, "course": "Rust"},
    "s5": {"name": "Anita", "age": 17, "course": "C++"}
}

restricted_courses = ["Java" , "Python"]

for student_id , info in students.items():
    if info["course"] not in restricted_courses and info["age"] >=  20 :
        print(info["name"])