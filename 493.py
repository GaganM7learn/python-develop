students = {
    "s1": {"name": "Arjun", "age": 18, "course": "C++"},
    "s2": {"name": "Nisha", "age": 22, "course": "Python"},
    "s3": {"name": "Kunal", "age": 24, "course": "C++"},
    "s4": {"name": "Priti", "age": 20, "course": "Python"},
    "s5": {"name": "Sameer", "age": 26, "course": "Java"},
    "s6": {"name": "Anu", "age": 22, "course": "Java"}
}

course_data = {}

for student_id , info in students.items():
    course = info["course"]

    if course not in course_data :
        course_data[course] ={
            'total_age' : 0,
            "count" : 0
        }
    course_data[course]["total_age"] += info["age"]
     
    course_data[course]["count"] += 1

for course , data in course_data.items():

    average_age = data['total_age']/data["count"]

    print(course , "Average age" , average_age )