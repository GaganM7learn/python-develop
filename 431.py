students ={
    "student1" : { 'name' : "Gagan" , "age" : 19 , "course" : "Python"},
    "student2" : { "name" : "Rahul" , "age" : 22 , 'course' : "Python"},
    "students3" : { "name" : "Amit" , "age" : 22 , "course" : "Java"}
}


for studdent_id , info in students.items():
    if info["age"] >= 20 and not info["course"] == "Python" :
        print(info["name"])