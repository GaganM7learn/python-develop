students = {
    "s1": {"name": "Asha", "age": 22, "city": "Pune", "course": "Python"},
    "s2": {"name": "Rohan", "age": 24, "course": "Java"},
    "s3": {"name": "Divya", "age": 21, "city": "Delhi"},
    "s4": {"name": "Manish", "age": 25},
    "s5": {"name": "Kavya", "age": 23, "city": "Mumbai", "course": "C++"}
}

for student_id , info in students.items():
    if "city" not in info or "course" not in info :
        print(info["name"] , "has no city or course information")