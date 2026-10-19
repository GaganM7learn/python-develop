products = [
    {"name": "Tablet", "price": 15000},
    {"name": "Mouse", "price": 800},
    {"name": "Monitor", "price": 12000}
]

result = sorted(products , key=lambda p: p["price"])

print(result)