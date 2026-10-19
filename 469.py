students = {
    "student1": {"name": "Gagan", "age": 19, "course": "Python"},
    "student2": {"name": "Rahul", "age": 21, "course": "Python"},
    "student3": {"name": "Amit", "age": 22, "course": "Java"},
    "student4": {"name": "Priya", "age": 18, "course": "Java"}
}

highest_age = 0
oldest_name = ""

for student_id , info in students.items():
    if info["age"] > highest_age : 
        highest_age = info["age"]
        oldest_name = info["name"]
print("Oldest student : " , oldest_name)
print("Age : " , highest_age )