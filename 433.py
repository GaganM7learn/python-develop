
for student_id , info in students.items():
    if info["age"] >= 20 and not info["course"] == "Java" : 
        print(info["name"])