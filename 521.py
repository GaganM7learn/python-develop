students = {
    "s1": {"name": "Rahul", "age": 22, "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "course": "Java"},
    "s3": {"name": "Arjun", "age": 23, "course": "C++"},
    "s4": {"name": "Pooja", "age": 21, "course": "SQL"},
    "s5": {"name": "Kiran", "age": 26, "course": "HTML"}
}

restricted_courses = ["Java" , "SQL"] 
selected_students = []

for student_id , info in students.items():
    if 20 <= info["age"]  <= 25 and info["course"] not in restricted_courses :
        selected_students.append(info['name'])

print(selected_students)