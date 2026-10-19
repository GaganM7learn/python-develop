students = {
    "s1": {"name": "Varun", "age": 23, "course": "Java"},
    "s2": {"name": "Riya", "age": 20, "course": "Python"},
    "s3": {"name": "Aditya", "age": 22, "course": "Java"},
    "s4": {"name": "Pallavi", "age": 19, "course": "C++"},
    "s5": {"name": "Harsh", "age": 24, "course": "Python"},
    "s6": {"name": "Anjali", "age": 21, "course": "Java"},
    "s7": {"name": "Mohan", "age": 18, "course": "C++"}
}
course_count = {}

for student_id , info in students.items():
    course = info['course']

    if course not in course_count:
        course_count[course] = 0

    course_count[course] += 1

print(course_count)