students = {
    "s1": {"name": "Rahul", "age": 22, "city": "Delhi"},
    "s2": {"name": "Meera", "age": 24, "course": "Python"},
    "s3": {"name": "Arjun", "age": 21, "city": "Mumbai", "course": "Java"},
    "s4": {"name": "Pooja", "age": 23}
}
for student_id , info in students.items():
    if 'city' in info or 'course' in info :
        print(info["name"] , "has city or course information")

        