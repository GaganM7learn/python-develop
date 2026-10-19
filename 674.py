deliveries = [
    {"name": "A", "region": "North", "packages": 8, "cost": 500, "status": "delivered"},
    {"name": "B", "region": "South", "packages": 3, "cost": 700, "status": "delivered"},
    {"name": "C", "region": "West", "packages": 10, "cost": 400, "status": "pending"},
    {"name": "D", "region": "East", "packages": 6, "cost": 600, "status": "delivered"},
    {"name": "E", "region": "North", "packages": 2, "cost": 900, "status": "delivered"}
]

blocked_regions = ["West", "South"]

total_cost = sum(
    delivery["packages"] * delivery["cost"]
    for delivery in deliveries
    if delivery["region"] not in blocked_regions
    and delivery["status"] == "delivered"
    and not (
        delivery["region"] == "East"
        and delivery["packages"] < 7
    )
)

print(total_cost)