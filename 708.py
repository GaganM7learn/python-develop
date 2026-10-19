orders = [
    {"item": "Laptop", "qty": 2, "price": 40000, "status": "paid"},
    {"item": "Mouse", "qty": 5, "price": 800, "status": "paid"},
    {"item": "Phone", "qty": 1, "price": 25000, "status": "pending"},
    {"item": "Monitor", "qty": 3, "price": 12000, "status": "paid"}
]

total = sum(
    o["qty"] * o["price"]
    for o in orders
    if o["status"] == "paid"
    and (o["qty"] >= 3 or o["price"] >= 30000)
)

print(total)