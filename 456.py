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
    },
    "student3": {
        "name": "Amit",
        "age": 22,
        "course": "Java",
        "city": "Delhi"
    }
}


del students["student3"]["city"]


print(students["student3"])