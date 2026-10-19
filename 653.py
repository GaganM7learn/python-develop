shipments = [
    {"name": "A", "region": "Central", "packages": 4, "cost": 300, "status": "delivered"},
    {"name": "B", "region": "Coastal", "packages": 7, "cost": 180, "status": "delivered"},
    {"name": "C", "region": "Mountain", "packages": 9, "cost": 120, "status": "delivered"},
    {"name": "D", "region": "Central", "packages": 6, "cost": 250, "status": "pending"},
    {"name": "E", "region": "Coastal", "packages": 3, "cost": 400, "status": "delivered"},
    {"name": "F", "region": "Central", "packages": 2, "cost": 500, "status": "delivered"}
]

blocked_regions = ["Mountain"]

total_shipment_cost = sum(
    item["packages"] * item["cost"]
    for item in shipments
    if item["region"] not in blocked_regions
    and item["status"] == "delivered"
    and ( item["region"] == "Central"
         or item["packages"] >= 5)
)
print(total_shipment_cost)