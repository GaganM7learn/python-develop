students = {
    "s1": {"name": "Rohan", "age": 20, "course": "C++"},
    "s2": {"name": "Priya", "age": 22, "course": "Python"},
    "s3": {"name": "Sameer", "age": 24, "course": "Go"},
    "s4": {"name": "Anjali", "age": 19, "course": "Java"},
    "s5": {"name": "Vivek", "age": 25, "course": "Rust"}
}

for student_id , info in students.items():
    if not ( info["course"] == "Python" or info["course"] == "Java") :
        print(info["name"])