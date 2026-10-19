students = {
    "s1": {"name": "Aman", "age": 22, "course": "Python"},
    "s2": {"name": "Riya", "age": 24, "course": "Java"},
    "s3": {"name": "Kabir", "age": 21, "course": "C++"},
    "s4": {"name": "Nisha", "age": 26, "course": "JavaScript"}
}

for student_id , info in students.items():
    if not (info["course"] == "Python" or info["course"] == "Java"):
     print(info["name"])