students = {
    "s1": {"name": "Asha", "age": 22, "city": "Mumbai"},
    "s2": {"name": "Kiran", "age": 24, "course": "Java"},
    "s3": {"name": "Neha", "age": 21, "city": "Pune", "course": "Python"},
    "s4": {"name": "Raj", "age": 25},
    "s5": {"name": "Divya", "age": 23, "course": "C++"}
}
for student_id , info in students.items():
    if "city" in info or "course" in info :
        print(info['name'] , "has city or course imformation")