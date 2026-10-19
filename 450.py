students = {
    "student1": {
        "name": "Gagan",
        "age": 19,
        "course": "Python"
    },
    "student2": {
        "name": "Rahul",
        "age": 21,
        "course": "Python"
    }
}

for student_id , info in students.items():
    if info["age"] >= 20 :
        info["status"] = "Adult"

    else :
        info["status"] = "Minor"

print(students)