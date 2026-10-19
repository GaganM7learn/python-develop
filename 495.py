students = {
    "s1": {"name": "Dev", "age": 19, "course": "Python"},
    "s2": {"name": "Lata", "age": 23, "course": "Python"},
    "s3": {"name": "Omkar", "age": 28, "course": "Java"},
    "s4": {"name": "Reena", "age": 24, "course": "Java"},
    "s5": {"name": "Tarun", "age": 21, "course": "C++"},
    "s6": {"name": "Simran", "age": 25, "course": "C++"}
}


course_data = {}

for student_id , info in students.items():
    course = info["course"]
    if course not in course_data :
        course_data[course] = {
            "total_age" :0,
            "count" :0
        }

    course_data[course]["total_age"] += info["age"]
    course_data[course]["count"] +=  1 

highest_average = 0
highest_course = ""

for course , data in course_data.items():
    average_age = data["total_age"]/ data["count"]

    if average_age > highest_average:
        highest_average = average_age
        highest_course = course

print("Course with Highest average " , highest_course)
print("with highest age average is " , highest_average)