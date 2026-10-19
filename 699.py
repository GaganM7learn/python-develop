orders = [
    {"item": "Monitor", "category": "Electronics", "qty": 3, "price": 12000, "status": "approved"},
    {"item": "Jeans", "category": "Clothing", "qty": 6, "price": 1800, "status": "approved"},
    {"item": "Table", "category": "Furniture", "qty": 4, "price": 7000, "status": "approved"},
    {"item": "Phone", "category": "Electronics", "qty": 1, "price": 30000, "status": "approved"},
    {"item": "Lamp", "category": "Home", "qty": 2, "price": 2500, "status": "pending"}
]

blocked_categories = ["Clothing"]

total = sum(
    p["qty"] * p["price"]
    for p in orders
    if p["category"] not in blocked_categories
    and p["status"] == "approved"
    and ( p["category"] == "Electronics" or p["qty"] >= 4)
    and not ( p["category"] == "Electronics" and p["qty"] < 2)
)

print(total)