students = {
    "student1": {"name": "Gagan", "age": 19, "course": "Python"},
    "student2": {"name": "Rahul", "age": 21, "course": "Python"},
    "student3": {"name": "Amit", "age": 22, "course": "Java"},
    "student4": {"name": "Priya", "age": 18, "course": "Java"}
}
oldest_studentname = ""
oldest_studentage = 0
for student_id , info in students.items():
    if info["age"] > oldest_studentage and info["course"] == "Java" :
        oldest_studentname = info["name"]
        oldest_studentage = info["age"]

print("Oldest Java student :" , oldest_studentname)
print("age :" , oldest_studentage)