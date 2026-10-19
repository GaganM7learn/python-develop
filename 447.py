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
    },
    "student3": {
        "name": "Amit",
        "age": 22,
        "course": "Java"
    }
}

for student_id , info in students.items():
    info["age"] = info["age"] +1 

print(students)