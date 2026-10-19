students = {
    "s1": {"name": "Rahul", "age": 22},
    "s2": {"name": "Meera", "age": 19},
    "s3": {"name": "Arjun", "age": 25},
    "s4": {"name": "Pooja", "age": 21}
}
sorted_students = sorted(
    students.items(),
    key=lambda item : item[1]["age"]
)


for student_id , info in sorted_students :
    print(info["name"] , info["age"])