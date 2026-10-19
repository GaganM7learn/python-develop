students = {
    "s1": {"name": "Arjun", "age": 17, "course": "Python"},
    "s2": {"name": "Meena", "age": 22, "course": "Java"},
    "s3": {"name": "Karan", "age": 16, "course": "C++"},
    "s4": {"name": "Priya", "age": 25, "course": "Python"},
    "s5": {"name": "Vijay", "age": 19, "course": "Java"}
}

grouped ={
    "under_age" : [],
    "18_or_above" : []
}

for student_id , info in students.items():
    if info['age'] < 18 :
        grouped["under_age"].append(info["name"])

    else :
        grouped["18_or_above"].append(info["name"])

print(grouped)