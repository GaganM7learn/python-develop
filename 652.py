deliveries = [
    {"name": "A", "region": "North", "packages": 5, "cost": 200, "status": "delivered"},
    {"name": "B", "region": "South", "packages": 2, "cost": 150, "status": "delivered"},
    {"name": "C", "region": "West", "packages": 8, "cost": 100, "status": "cancelled"},
    {"name": "D", "region": "East", "packages": 6, "cost": 180, "status": "delivered"},
    {"name": "E", "region": "North", "packages": 3, "cost": 250, "status": "pending"}
]

blocked_regions = ["West"]

total_delivery_cost = sum(
    delivery['packages'] * delivery["cost"]
    for delivery in deliveries
    if delivery['region'] not in blocked_regions
    and delivery["status"] == "delivered"
    and (
        delivery["region"] == "North"
        or delivery['packages'] >= 5
    )
)

print(total_delivery_cost)