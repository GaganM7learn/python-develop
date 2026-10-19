students = {
    "s1": {"name": "Asha", "age": 23, "course": "Go"},
    "s2": {"name": "Ravi", "age": 19, "course": "Java"},
    "s3": {"name": "Nisha", "age": 27, "course": "Rust"},
    "s4": {"name": "Vijay", "age": 16, "course": "Python"},
    "s5": {"name": "Deepa", "age": 24, "course": "C++"}
}

blocked_courses = ["Java" , "C++"]

for student_id , info in students.items():
    if (not info["course"] in blocked_courses and info["age"] >= 21) or info["age"] < 18 :
        print(info["name"])