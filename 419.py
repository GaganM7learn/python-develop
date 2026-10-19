students = {
    "student1" : {
        "name" : "  Gagan" , 
        "age" : 19,
        "city" : "Bangalore"
    }
}

removed = students["student1"].pop("age")

print(removed)
print(students)