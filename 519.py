students = {
    "s1": {"name": "Rahul", "age": 21, "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "course": "Java"},
    "s3": {"name": "Arjun", "age": 23, "course": "C++"},
    "s4": {"name": "Pooja", "age": 26, "course": "SQL"},
    "s5": {"name": "Kiran", "age": 19, "course": "JavaScript"}
}

selected_students = []
allowed_course = ['Python' , "Java" , "C++"]

for student_id ,info in students.items():
    if 20 <= info["age"] <= 25 and info["course"] in allowed_course :
        selected_students.append(info["name"])

print(selected_students)