students = {
    "student1": {"name": "Gagan", "age": 19, "course": "Python"},
    "student2": {"name": "Rahul", "age": 21, "course": "Python"},
    "student3": {"name": "Amit", "age": 22, "course": "Java"},
    "student4": {"name": "Priya", "age": 18, "course": "Java"}
}
to_remove = []


for student_id , info in students.items():
    if info["age"] >= 20 or info["course"] == "Java" :
        to_remove.append(student_id)

for student_id in to_remove:
    del students[student_id]

print(students)