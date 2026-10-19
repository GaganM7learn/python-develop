import json
product = {
    "name": "Keyboard",
    "price": 2500,
    "in_stock": True
}

with open("product.json" , "w") as file :
    json.dump(product , file)

print("Saved")