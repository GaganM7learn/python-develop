students = {
    "s1": {"name": "Aarav", "age": 21, "course": "Python"},
    "s2": {"name": "Meera", "age": 24, "course": "Java"},
    "s3": {"name": "Kabir", "age": 27, "course": "Python"},
    "s4": {"name": "Naveen" , "age" : 23, "course": "C++"},
    "s5": {"name": "Diya", "age": 20, "course": "Java"},
    "s6": {"name": "Arjun", "age": 26, "course": "Python"}
}


selected_students = []

for student_id , info in students.items():
    if 20<= info["age"] <= 25 and (info["course"] == "Python" or info["course"] == "Java"):
        selected_students.append(info["name"])

print(selected_students)