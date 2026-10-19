students = {
    "s1": {"name": "Asha", "age": 23, "course": "Go"},
    "s2": {"name": "Vikram", "age": 19, "course": "Java"},
    "s3": {"name": "Nisha", "age": 26, "course": "Rust"},
    "s4": {"name": "Karan", "age": 17, "course": "Python"},
    "s5": {"name": "Divya", "age": 21, "course": "C++"}
}

technical_courses = ["Go" , "Rust" , "C++"]

for student_id , info in students.items():
    if ( info["course"] in technical_courses and info["age"] >= 21 ) or info["age"] < 18 :
        print(info["name"])