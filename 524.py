students = {
    "s1": {"name": "Asha", "age": 22, "city": "Delhi"},
    "s2": {"name": "Ravi", "age": 24, "course": "Python"},
    "s3": {"name": "Nisha", "age": 21, "city": "Chennai"},
    "s4": {"name": "Karan", "age": 25, "course": "Java"},
    "s5": {"name": "Divya", "age": 23, "city": "Pune"}
}
selected_student = []
for student_id ,info in students.items():
    if "city" in info :
        print(info["name"], "has city information")