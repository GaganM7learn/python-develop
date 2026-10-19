students = {
    "s1": {"name": "Aarav", "age": 20, "course": "Python"},
    "s2": {"name": "Maya", "age": 24, "course": "Python"},
    "s3": {"name": "Rohan", "age": 25, "course": "Java"},
    "s4": {"name": "Sneha", "age": 27, "course": "Java"},
    "s5": {"name": "Kiran", "age": 18, "course": "C++"},
    "s6": {"name": "Pooja", "age": 20, "course": "C++"}
}

course_data = {}

for student_id , info in students.items():
    course = info["course"]
    if course not in course_data :
        course_data[course] ={
            "total_age" : 0,
            "count" : 0
        }

    course_data[course]["total_age"] += info['age']
    course_data[course]["count"] += 1
highest_average = 0

highest_course = ""

for course , data in course_data.items():
    average_age = data["total_age"]/data["count"]

    if average_age > highest_average :
        highest_average = average_age
        highest_course = course

print('Course:' , highest_course)
print("Highest Average Age :" , highest_average)