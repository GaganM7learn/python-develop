students = {
    "student1": {"name": "Gagan", "age": 19, "course": "Python"},
    "student2": {"name": "Rahul", "age": 21, "course": "Python"},
    "student3": {"name": "Amit", "age": 22, "course": "Java"},
    "student4": {"name": "Priya", "age": 18, "course": "Java"}
}

total_age = 0 
count = 0

for student_id , info in students.items():
    if info["course"] == "Python" :
        total_age = total_age + info["age"]
        count = count + 1
        average_age = total_age/count # average should be in the first line


print("Average Python age :" , average_age )


