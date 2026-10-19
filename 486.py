students = {
    "s1": {"name": "Nikhil", "age": 15, "course": "Python"},
    "s2": {"name": "Asha", "age": 20, "course": "Java"},
    "s3": {"name": "Rahul", "age": 17, "course": "C++"},
    "s4": {"name": "Kavya", "age": 23, "course": "Python"},
    "s5": {"name": "Deepak", "age": 16, "course": "Java"},
    "s6": {"name": "Sonia", "age": 21, "course": "C++"}
}

grouped = {
    "under_18" : [],
    "18_or_above" : []
}

for student_id , info in students.items():
    if info["age"] < 18 :
        grouped["under_18"].append(info["name"])
    else :
        grouped["18_or_above"].append(info["name"])

print(grouped)