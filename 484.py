students = {
    "s1": {"name": "Rohan", "age": 26, "course": "C++"},
    "s2": {"name": "Anita", "age": 22, "course": "Python"},
    "s3": {"name": "Manoj", "age": 25, "course": "C++"},
    "s4": {"name": "Divya", "age": 21, "course": "Java"},
    "s5": {"name": "Suresh", "age": 23, "course": "Python"},
    "s6": {"name": "Pooja", "age": 24, "course": "Java"}
}

grouped = {}
for  student_id , info in students.items():
    if info["course"] not in grouped :
        grouped[info["course"]] = []
    grouped[info["course"]].append(info["name"])

print(grouped)