products = [
    {"name": "Laptop", "price": 50000, "qty": 2, "status": "sold"},
    {"name": "Mouse", "price": 800, "qty": 5, "status": "sold"},
    {"name": "Camera", "price": 30000, "qty": 1, "status": "pending"},
    {"name": "Monitor", "price": 12000, "qty": 3, "status": "sold"}
]

total = sum(
    p["price"] * p["qty"]
    for p in products
    if p["status"] == "sold"
    and (p["qty"] >= 3 or p["price"] >= 20000)
)

print(total)  # 136000