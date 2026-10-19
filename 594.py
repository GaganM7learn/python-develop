students = {
    "s1": {"name": 1, "age": 22},
    "s2": {"name": 2, "age": 19},
    "s3": {"name": 5, "age": 25},
    "s4": {"name":8, "age": 21}
}

sorted_students = sorted(
    students.items(),
    key=lambda item: item[0]["name"]
)

for student_id, info in sorted_students:
    print(info["name"], info["age"])