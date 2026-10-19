import json
text = '{ "name" : "Ava" , "age" : 21}'
data = json.loads(text)
print(data["name"])
print(data["age"])