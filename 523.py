students = {
    "s1": {"name": "Rahul", "age": 22, "city": "Bangalore"},
    "s2": {"name": "Meera", "age": 24},
    "s3": {"name": "Arjun", "age": 21, "city": "Mumbai"},
    "s4": {"name": "Pooja", "age": 23}
}

for student_id , info in students.items():
    if "city" in info :
        print(info["name"] , "has city information")