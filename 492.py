students = {
    "s1": {"name": "Aman", "age": 20, "course": "Python"},
    "s2": {"name": "Kavita", "age": 24, "course": "Python"},
    "s3": {"name": "Raj", "age": 22, "course": "Java"},
    "s4": {"name": "Simran", "age": 26, "course": "Java"}
}

course_data = {}

for student_id , info in students.items():
    course = info["course"]

    if course not in course_data:
        course_data[course] = {
            "total_age" : 0 ,
            "count" : 0
        }
    course_data[course]["count"] += 1
    course_data[course]["total_age"] += info["age"]

for course , data in course_data.items():
    average_age = data["total_age"]/data["count"]

    print(course , "Average Age : ", average_age )