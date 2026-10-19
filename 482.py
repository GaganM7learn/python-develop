students = {
    "s1": {"name": "Arjun", "age": 24, "course": "Python"},
    "s2": {"name": "Neha", "age": 20, "course": "Java"},
    "s3": {"name": "Kiran", "age": 23, "course": "Python"},
    "s4": {"name": "Sneha", "age": 19, "course": "Java"}
}

grouped = {}

for student_id , info in students.items():
    if info["course"] not in grouped :
        grouped[info["course"]] = []

    grouped[info["course"]].append(info["name"])

print(grouped)