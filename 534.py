students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "city": "Mumbai"},
    "s3": {"name": "Arjun", "age": 21, "city": "Delhi", "course": "Java"},
    "s4": {"name": "Pooja", "age": 23},
    "s5": {"name": "Kiran", "age": 25, "course": "C++"}
}

for student_id , info in students.items():
    if "city" not in info or 'course' not in info:
        print(info["name"] , "has no city or course in information")