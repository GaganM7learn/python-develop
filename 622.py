laptops = [
    {"model": "Dell Inspiron", "price": 62000, "ram": 16, "rating": 4.3},
    {"model": "HP Pavilion", "price": 58000, "ram": 8, "rating": 4.5},
    {"model": "Lenovo IdeaPad", "price": 55000, "ram": 16, "rating": 4.6},
    {"model": "Asus Vivobook", "price": 70000, "ram": 32, "rating": 4.7},
    {"model": "Acer Aspire", "price": 48000, "ram": 16, "rating": 4.2}
]

best_budget_laptop = min( (laptop for laptop in laptops
                         if laptop["ram"] >= 16 and 
                         laptop["rating"] >= 4.5 ) , key=lambda laptop : laptop["price"] )

print(best_budget_laptop)