import json
text = '{"city": "Pune", "population": 7000000}'

data = json.loads(text)

print(data["city"])
print(data["population"])