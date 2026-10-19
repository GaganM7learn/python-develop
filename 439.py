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
        "age": 22
    }
}

for student_id , info in students.items():
    if "course" in info:
        print(info["name"])