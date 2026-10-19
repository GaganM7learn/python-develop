students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 17, "course": "Java"},
    "s3": {"name": "Arjun", "age": 25, "course": "C++"},
    "s4": {"name": "Pooja", "age": 19, "course": "Java"}
}

for student_id , info in students.items():
    if (not info["course"] == "Java" and info["age"] >= 20) or info["age"] < 18 :
        print(info["name"])