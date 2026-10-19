students = {
    "s1": {"name": "Aman", "age": 20, "course": "Go"},
    "s2": {"name": "Divya", "age": 23, "course": "Rust"},
    "s3": {"name": "Nitin", "age": 27, "course": "C++"},
    "s4": {"name": "Kavya", "age": 18, "course": "Python"},
    "s5": {"name": "Suresh", "age": 24, "course": "Java"}
}

target_courses = ["C++" , "Rust"] 

for student_id , info in students.items():
    if info["course"] in target_courses or info["age"] >= 26 :
        print(info["name"])