students = {
    "s1": {"name": "Aisha", "age": 21, "course": "Python"},
    "s2": {"name": "Rahul", "age": 29, "course": "Java"},
    "s3": {"name": "Meera", "age": 24, "course": "C++"},
    "s4": {"name": "Vijay", "age": 26, "course": "Python"},
    "s5": {"name": "Neha", "age": 27, "course": "Java"}
}

highest_age = 0
oldest_student = {}

for student_id , info in students.items():
    if info["age"] > highest_age :
        highest_age = info["age"]


        oldest_student = {
            "name" : info["name"],
            "age" : info["age"],
            "course" : info["course"]
        }

print(oldest_student)