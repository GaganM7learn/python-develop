students = {
    "s1": {"name": "Aarav", "age": 20, "course": "Python"},
    "s2": {"name": "Isha", "age": 22, "course": "Java"},
    "s3": {"name": "Ravi", "age": 19, "course": "Python"},
    "s4": {"name": "Neha", "age": 24, "course": "C++"},
    "s5": {"name": "Kabir", "age": 21, "course": "Java"}
}

course_count = {}

for student_id , info in students.items():
    course = info["course"]

    if course not in course_count :
        course_count[course] = 0

    course_count[course] += 1 

print(course_count)