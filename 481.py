students = {
    "student1": {"name": "Gagan", "age": 19, "course": "Python"},
    "student2": {"name": "Rahul", "age": 21, "course": "Python"},
    "student3": {"name": "Amit", "age": 22, "course": "Java"},
    "student4": {"name": "Priya", "age": 18, "course": "Java"},
    "student5": {"name": "Ravi", "age": 20, "course": "Python"}
}

python_count = 0
java_count = 0
for student_id , info in students.items():
    if info["course"] == "Python" :
        python_count = python_count + 1

    elif info["course"] == "Java" :
        java_count = java_count + 1
        if python_count > java_count :
            print("Python as more students")
        elif java_count > python_count :
            print("Java as more students")