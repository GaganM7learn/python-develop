students = {
    "s1": {"name": "Aarav", "age": 23, "course": "Python"},
    "s2": {"name": "Isha", "age": 19, "course": "Java"},
    "s3": {"name": "Rohan", "age": 25, "course": "C++"},
    "s4": {"name": "Tina", "age": 21, "course": "Python"},
    "s5": {"name": "Kunal", "age": 18, "course": "Java"}
}

youngest_age = 999
youngest_student = {}

for student_id , info in students.items():
    if info["age"] < youngest_age :
        lowest_age = info["age"]

        youngest_student = {
            "name" : info["name"], 
            "age" : info['age'],
            "course" : info["course"]
        }

print(youngest_student)