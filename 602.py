products = [
    {"name": "Laptop", "category": "Electronics", "price": 70000},
    {"name": "Phone", "category": "Electronics", "price": 40000},
    {"name": "Chair", "category": "Furniture", "price": 12000},
    {"name": "Table", "category": "Furniture", "price": 18000}
]

sorted_products = sorted( products , key=lambda product : (product["category"] ,product["price"]) , reverse=True)
print(sorted_products)