students = {
    "s1": {"name": "Riya", "age": 21, "course": "Python"},
    "s2": {"name": "Amit", "age": 23, "course": "Java"},
    "s3": {"name": "Sneha", "age": 25, "course": "C++"},
    "s4": {"name": "Vikas", "age": 19, "course": "SQL"},
    "s5": {"name": "Priti", "age": 24, "course": "HTML"},
    "s6": {"name": "Rohan", "age": 26, "course": "JavaScript"}
}

restricted_courses = ["Java" , "SQL" , "JavaScript"]

selected_students = []

for student_if , info in students.items():
    if 21 <= info["age"] <= 25 and info["course"] not in restricted_courses :
        selected_students.append(info["name"])
print(selected_students)