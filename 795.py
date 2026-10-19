import json
student = { "name" : "Ava" , "score" : 92}
with open("student.json" , "w") as file :
    json.dump(student , file)


print("Saved")