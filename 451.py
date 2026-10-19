students = {
    "student1": {
        "name": "Gagan",
        "age": 19,
        "course": "Python"
    },
    "student2": {
        "name": "Rahul",
        "age": 21,
        "course": "Java"
    }
}

for student_id , info in students.items() :
    if info["course"] == "Pyhton" : 
        info["level"] = "Programming"

    else :
        info["level"] = "Other"

print(students)