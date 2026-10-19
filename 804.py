import json 
with open("game.json" , "r") as file :
    sloth = json.load(file)

print(sloth["player"])
print(sloth["level"])
print(sloth["lives"])