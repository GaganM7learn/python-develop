products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Phone", "price": 45000},
    {"name": "Tablet", "price": 30000},
    {"name": "Monitor", "price": 18000}
]

sorted_products = sorted( products , key=lambda item: item["price"], reverse=True )
print(sorted_products)