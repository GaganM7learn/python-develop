shipments = [
    {"name": "Keyboard", "category": "Electronics", "price": 3000, "quantity": 5, "status": "delivered"},
    {"name": "Wardrobe", "category": "Furniture", "price": 22000, "quantity": 1, "status": "delivered"},
    {"name": "Cap", "category": "Fashion", "price": 800, "quantity": 10, "status": "delivered"},
    {"name": "Speaker", "category": "Electronics", "price": 6500, "quantity": 2, "status": "pending"},
    {"name": "Bookshelf", "category": "Furniture", "price": 9000, "quantity": 4, "status": "delivered"},
    {"name": "Mouse", "category": "Electronics", "price": 1200, "quantity": 3, "status": "delivered"}
]

blocked_categories = ["Fashion"]

total_value = sum(
    ship["price"] * ship["quantity"]
    for ship in shipments
    if ship["category"] not in blocked_categories
    and ship["status"] == "delivered"
    and (
        ship["category"] == "Electronics"
        or ship["quantity"] >= 3
    )
)
print(total_value)