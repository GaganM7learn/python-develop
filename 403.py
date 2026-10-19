students = {
    'student1' : {
        "name" : "Gagan" , 
        "age" : 19
    }, 
    'student2' : {
        "name" : "Rahul" ,
        "age" : 20
    }
}

for student_id , info in students.items():
    print(student_id)

    for key , value in info.items():
        print(key , value)