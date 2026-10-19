students = {
    "student1": {
        "name": "Gagan",
        "age": 19
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}

for student_id , info in students.items():
    if info["age"] >= 20 :
        print(info["name"] , "is 20 or older")