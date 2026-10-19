students = {
    "s1": {"name": "Nisha", "age": 22, "course": "Python"},
    "s2": {"name": "Amit", "age": 24, "city": "Delhi"},
    "s3": {"name": "Riya", "age": 21, "course": "Java", "city": "Pune"},
    "s4": {"name": "Karan", "age": 25, "course": "C++"},
    "s5": {"name": "Tina", "age": 23},
    "s6": {"name": "Vivek", "age": 26, "city": "Mumbai", "course": "SQL"}
}

for student_id ,info in students.items():
    if "city" not in info and "course" in info :
        print(info["name"] , "has course but not the city")