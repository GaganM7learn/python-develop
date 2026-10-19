students = {
    "s1": {"name": "Rahul", "age": 22, "city": "Delhi"},
    "s2": {"name": "Meera", "age": 24},
    "s3": {"name": "Arjun", "age": 21, "course": "Python"},
    "s4": {"name": "Pooja", "age": 23}
}

for student_id ,info in students.items():
    if 'city' not in info :
        print(info["name"] , "does not have city information" )