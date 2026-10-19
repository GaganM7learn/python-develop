products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Phone", "price": 45000},
    {"name": "Tablet", "price": 30000}
]

cheapest = min( products , key=lambda product : product["price"])
expensive = max(products , key=lambda product : product["price"])

print(cheapest)
print(expensive)