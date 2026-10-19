students = {
    "s1": {"name": "Rohan", "age": 21, "course": "Python"},
    "s2": {"name": "Meena", "age": 24, "course": "Java"},
    "s3": {"name": "Karan", "age": 20, "course": "Python"},
    "s4": {"name": "Divya", "age": 22, "course": "Java"}
}

grouped = {}

for student_id , info in students.items():
    course = info["course"]

    if course not in grouped :
        grouped[course] = []

    grouped[course].append({
        "name" : info["name"],
        "age" : info["age"]
    })
print(grouped)