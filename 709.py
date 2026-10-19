purchases = [
    {"item": "Tablet", "qty": 4, "price": 15000, "status": "approved"},
    {"item": "Keyboard", "qty": 2, "price": 2500, "status": "approved"},
    {"item": "Camera", "qty": 1, "price": 42000, "status": "approved"},
    {"item": "Chair", "qty": 5, "price": 6000, "status": "pending"},
    {"item": "Phone", "qty": 2, "price": 22000, "status": "approved"}
]

total = sum(
    o["qty"] * o["price"]
    for o in purchases
    if o["status"] == "approved"
    and (o["qty"] >= 3 or o["price"] >= 20000)
)

print(total)