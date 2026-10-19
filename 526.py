students = {
    "s1": {"name": "Kavya", "age": 23, "city": "Mumbai"},
    "s2": {"name": "Rohan", "age": 21, "course": "Python"},
    "s3": {"name": "Isha", "age": 25, "city": "Pune"},
    "s4": {"name": "Manoj", "age": 24, "course": "Java"},
    "s5": {"name": "Tina", "age": 22}
}

for student_id , info in students.items() :
    if 'city' not in info :
        print(info["name"] , "City information is not given")