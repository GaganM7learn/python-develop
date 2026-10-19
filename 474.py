students = {
    "student1": {"name": "Gagan", "age": 19, "course": "Python"},
    "student2": {"name": "Rahul", "age": 21, "course": "Python"},
    "student3": {"name": "Amit", "age": 22, "course": "Java"},
    "student4": {"name": "Priya", "age": 18, "course": "Java"}
}

lowest_age = 999
youngest_name = ""

for student_id , info in students.items():

    if info["age"] < lowest_age and info["course"] == "Java":
        lowest_age = info["age"]
        youngest_name = info["name"]
print("Youngest Java Student :" , youngest_name)

print("Age :" , lowest_age)