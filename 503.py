students = {
    "s1": {"name": "Aman", "age": 21, "course": "Python"},
    "s2": {"name": "Priya", "age": 28, "course": "Java"},
    "s3": {"name": "Karan", "age": 19, "course": "C++"},
    "s4": {"name": "Neha", "age": 24, "course": "Python"},
    "s5": {"name": "Vikas", "age": 32, "course": "Java"}
}
highest_age = 0
lowest_age = 999

oldest_student = {}
youngest_student = {}

for student_id , okay in students.items():
    if okay["age"] > highest_age :
        highest_age = okay["age"]

        oldest_student = {
            "name" : okay["name"] , 
            "age" : okay["age"],
            "course" :okay["course"]
        }

    if okay["age"] < lowest_age :
        lowest_age = okay["age"]

        youngest_student = {
            "name" : okay["name"],
            "age" : okay["age"], 
            "course" :okay["course"] 
        }
print("Oldest :", oldest_student)
print("Youngest :" , youngest_student)