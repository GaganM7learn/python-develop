cars = [
    {"model": "Honda City", "price": 1200000, "year": 2022, "mileage": 18},
    {"model": "Hyundai Creta", "price": 1500000, "year": 2021, "mileage": 16},
    {"model": "Tata Nexon", "price": 950000, "year": 2023, "mileage": 20},
    {"model": "Kia Seltos", "price": 1400000, "year": 2024, "mileage": 17},
    {"model": "Maruti Brezza", "price": 1100000, "year": 2020, "mileage": 19}
]

cheapest_car = min(( car for car in cars if car["year"] >= 2022 and car["mileage"] >= 18) , key=lambda car : car["price"] )
print(cheapest_car)