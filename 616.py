products = [
    {"name": "Keyboard", "price": 2500, "stock": 10},
    {"name": "Mouse", "price": 1200, "stock": 0},
    {"name": "Headphones", "price": 3500, "stock": 6},
    {"name": "Webcam", "price": 2800, "stock": 0},
    {"name": "Speaker", "price": 4200, "stock": 4}
]

most_expensive_available = max((product for product in products if product["stock"] > 0 ) , key=lambda product : product["price"])
print(most_expensive_available)