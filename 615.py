products = [
    {"name": "Laptop", "price": 75000, "stock": 5},
    {"name": "Phone", "price": 45000, "stock": 0},
    {"name": "Tablet", "price": 30000, "stock": 8},
    {"name": "Monitor", "price": 18000, "stock": 3}
]
cheapest_available = min( (product for product in products if product["stock"] > 0) , key=lambda product: product["price"])

print(cheapest_available)