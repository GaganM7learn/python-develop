students = {
    "student1": {
        "name": "Gagan",
        "age": 19,
        "course": "Python"
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    },
    "student3": {
        "name": "Amit",
        "age": 22,
        "course": "Java"
    }
}


for student_id , info in students.items():
    if info.get("course") == "Python" : 
        print(info["name"])