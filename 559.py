students = {
    "s1": {"name": "Neha", "age": 20, "course": "Go"},
    "s2": {"name": "Ravi", "age": 23, "course": "Python"},
    "s3": {"name": "Sneha", "age": 25, "course": "Java"},
    "s4": {"name": "Amit", "age": 22, "course": "Rust"},
    "s5": {"name": "Priya", "age": 19, "course": "C++"}
}

blocked_courses = ["Java" , "Python"]

preferred_courses = ["Go" , "Rust" , "C++"]

for student_id , info in students.items():
    
    if info["course"] in preferred_courses and info["course"] not in blocked_courses :
        print(info["name"])