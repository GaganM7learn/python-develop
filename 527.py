students = {
    "s1": {"name": "Rahul", "age": 22, "city": "Delhi", "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "city": "Mumbai"},
    "s3": {"name": "Arjun", "age": 21, "course": "Java"},
    "s4": {"name": "Pooja", "age": 23, "city": "Pune", "course": "C++"}
}
for student_id ,info in students.items():
    if "city" in info and "course" in info :
        print(info['name'] , " has both city and course information ")