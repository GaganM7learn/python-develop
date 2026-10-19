students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 19, "course": "Java"},
    "s3": {"name": "Arjun", "age": 25, "course": "C++"},
    "s4": {"name": "Pooja", "age": 17, "course": "Python"}
}
for student_id , info in students.items():
    if not info["course"] == "Python" or info["age"] < 18 :
        print(info["name"])