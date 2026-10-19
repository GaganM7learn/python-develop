shipments = [
    {"item": "Laptop", "category": "Electronics", "quantity": 3, "price": 40000, "status": "delivered"},
    {"item": "Chair", "category": "Furniture", "quantity": 6, "price": 5000, "status": "delivered"},
    {"item": "Shoes", "category": "Fashion", "quantity": 8, "price": 2500, "status": "delivered"},
    {"item": "Phone", "category": "Electronics", "quantity": 2, "price": 30000, "status": "cancelled"},
    {"item": "Desk", "category": "Furniture", "quantity": 2, "price": 15000, "status": "delivered"},
    {"item": "Monitor", "category": "Electronics", "quantity": 4, "price": 18000, "status": "delivered"}
]

blocked_categories = ["Fashion"]

total_shipment_value = sum(
    shipment["quantity"] * shipment["price"]
    for shipment in shipments
    if shipment["category"] not in blocked_categories
    and (
        shipment["category"] == "Electronics"
        or shipment["quantity"] >= 5

    )
    and shipment["status"] == "delivered"
)

print(total_shipment_value)