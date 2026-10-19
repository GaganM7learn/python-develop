parcels = [
    {"name": "P1", "region": "Central", "packages": 9, "cost": 350, "status": "delivered"},
    {"name": "P2", "region": "Coastal", "packages": 4, "cost": 800, "status": "delivered"},
    {"name": "P3", "region": "Mountain", "packages": 12, "cost": 450, "status": "delivered"},
    {"name": "P4", "region": "Central", "packages": 5, "cost": 600, "status": "pending"},
    {"name": "P5", "region": "Coastal", "packages": 8, "cost": 500, "status": "delivered"},
    {"name": "P6", "region": "Mountain", "packages": 3, "cost": 700, "status": "delivered"}
]

blocked_regions = ["Mountain"]
total_cost = sum(
    parcel['packages'] * parcel["cost"]
    for parcel in parcels
    if parcel['region'] not in blocked_regions
    and parcel["status"] == "delivered"
    and not ( parcel["region"] == "Coastal" and parcel["packages"] < 6)
)


print(total_cost)