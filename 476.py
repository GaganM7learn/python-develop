students = {
    "student1": {"name": "Gagan", "age": 19, "course": "Python"},
    "student2": {"name": "Rahul", "age": 21, "course": "Python"},
    "student3": {"name": "Amit", "age": 22, "course": "Java"},
    "student4": {"name": "Priya", "age": 18, "course": "Java"}
}


total_age = 0
for student_id , info in students.items():
    total_age = total_age + info["age"]

average_age = total_age/len(students)


print("Average age :" , average_age)