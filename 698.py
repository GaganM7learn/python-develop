purchases = [
    {"item": "Laptop", "category": "Electronics", "qty": 2, "price": 40000, "status": "approved"},
    {"item": "Shirt", "category": "Clothing", "qty": 5, "price": 1200, "status": "approved"},
    {"item": "Desk", "category": "Furniture", "qty": 3, "price": 8000, "status": "approved"},
    {"item": "Phone", "category": "Electronics", "qty": 1, "price": 25000, "status": "pending"}
]

blocked_categories = ["Clothing"]

total = sum(
    p["qty"] * p["price"]
    for p in purchases
    if p["category"] not in blocked_categories
    and p["status"] == "approved"
    and (
        p["category"] == "Electronics"
        or p["qty"] >= 3
    )
    and not (
        p["category"] == "Electronics"
        and p["qty"] < 2
    )
)

print(total)