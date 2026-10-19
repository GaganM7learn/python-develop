students = {
    "s1": {"name": "Pavan", "age": 21, "course": "Go"},
    "s2": {"name": "Isha", "age": 17, "course": "Python"},
    "s3": {"name": "Rohit", "age": 24, "course": "Java"},
    "s4": {"name": "Sneha", "age": 26, "course": "Rust"},
    "s5": {"name": "Manu", "age": 16, "course": "C++"}
}

blocked_courses = ["Python" , 'Java']

for student_id , info in students.items():
    if info["course"] not in blocked_courses or info["age"] < 18 :
        print(info["name"])