students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "city": "Mumbai", "course": "Java"},
    "s3": {"name": "Arjun", "age": 21, "course": "C++"},
    "s4": {"name": "Pooja", "age": 23, "city": "Delhi"},
    "s5": {"name": "Kiran", "age": 25}
}

for student_id , info in students.items():
    if "city" not in info and "course" in info :
        print(info["name"] , "has course cut not city")