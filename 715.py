products = [
    {"name": "Phone", "price": 22000, "qty": 2, "status": "sold"},
    {"name": "Desk", "price": 18000, "qty": 1, "status": "sold"},
    {"name": "Camera", "price": 40000, "qty": 1, "status": "sold"},
    {"name": "Keyboard", "price": 3000, "qty": 4, "status": "pending"},
    {"name": "Tablet", "price": 15000, "qty": 3, "status": "sold"}
]

total = sum(
    p["price"]
    for p in products
    if p["status"] == "sold"
    and ( p["qty"] >= 2 or p["price"] == 25000)
)

print(total)