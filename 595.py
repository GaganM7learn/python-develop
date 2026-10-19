students = {
    "s1": {"name": "Neha", "age": 23},
    "s2": {"name": "Arun", "age": 31},
    "s3": {"name": "Priti", "age": 20},
    "s4": {"name": "Sameer", "age": 27},
    "s5": {"name": "Kavya", "age": 25}
}
sorted_age = sorted(
    students.items(),
    key=lambda item : item[1]["age"] , reverse=True
)

for student_id ,info in sorted_age :
    print(info["name"] , info["age"])