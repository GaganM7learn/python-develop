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
    },
    "student4": {
        "name": "Priya",
        "age": 18
    }
}

for student_id , info in students.items():
    course = info.get("course" , "Not assigned")

    if course == "Not assigned" : 
        print(info["name"] )