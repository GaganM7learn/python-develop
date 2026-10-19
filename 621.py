phones = [
    {"model": "Pixel 9", "price": 75000, "storage": 256, "rating": 4.5},
    {"model": "Galaxy S25", "price": 85000, "storage": 512, "rating": 4.7},
    {"model": "iPhone 16", "price": 90000, "storage": 256, "rating": 4.6},
    {"model": "OnePlus 13", "price": 65000, "storage": 512, "rating": 4.4},
    {"model": "Nothing Phone", "price": 45000, "storage": 256, "rating": 4.3}
]

premium_phone = max(( phone for phone in phones 
                      if phone["storage"] >= 256 and phone["rating"] >= 4.5 ) , key=lambda phone : phone["price"])
print(premium_phone)