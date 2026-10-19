students = {
    "s1": {"name": "Riya", "age": 22, "course": "Python"},
    "s2": {"name": "Sameer", "age": 24, "course": "JavaScript"},
    "s3": {"name": "Anjali", "age": 26, "course": "Java"},
    "s4": {"name": "Harish", "age": 21, "course": "Python"},
    "s5": {"name": "Kavya", "age": 25, "course": "Java"},
    "s6": {"name": "Mohan", "age": 28, "course": "Python"}
}
selected_students = []

for student_id , info in students.items():
    if 22 <= info["age"] <= 26 and (info["course"] == "Java" or info["course"] == "Python") and not info["course"] == "JavaScript " : 
        selected_students.append(info["name"]) 

print(selected_students)