inventory = [
    {"name": "Tablet", "category": "Electronics", "quantity": 5, "price": 22000, "status": "available"},
    {"name": "Bed", "category": "Furniture", "quantity": 7, "price": 18000, "status": "available"},
    {"name": "Jeans", "category": "Fashion", "quantity": 10, "price": 3000, "status": "available"},
    {"name": "Camera", "category": "Electronics", "quantity": 2, "price": 35000, "status": "reserved"},
    {"name": "Cupboard", "category": "Furniture", "quantity": 3, "price": 25000, "status": "available"},
    {"name": "Smartwatch", "category": "Electronics", "quantity": 4, "price": 9000, "status": "available"}
]

blocked_categories = ["Fashion"]

total_inventory_value = sum(
    item["quantity"] * item["price"]
    for item in inventory
    if item["category"] not in blocked_categories
    and ( item["category"] == "Electronics"
         or item["quantity"] >= 6)

         and item["status"] == "available"
)

print(total_inventory_value)