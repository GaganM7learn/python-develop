students = {
    "student1": {
        "name": "Gagan",
        "age": 19,
        "course": "Python",
        "city": "Bangalore"
    },
    "student2": {
        "name": "Rahul",
        "age": 21,
        "course": "Python",
        "city": "Mumbai"
    }
}


del students["student1"]["city"]

print(students["student1"])