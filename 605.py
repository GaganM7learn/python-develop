cars = [
    {"name": "Toyota", "price": 1800000},
    {"name": "Honda", "price": 2200000},
    {"name": "Tata", "price": 1500000},
    {"name": "Hyundai", "price": 1950000}
]

cheapest_car = min( cars , key=lambda car : car["price"])
expensive_car = max( cars , key=lambda car : car["price"])

print(cheapest_car)
print(expensive_car)