deliveries = [
    {"region": "Coastal", "packages": 7, "rate": 280, "status": "delivered"},
    {"region": "Mountain", "packages": 9, "rate": 400, "status": "delivered"},
    {"region": "Coastal", "packages": 3, "rate": 220, "status": "delivered"},
    {"region": "Central", "packages": 8, "rate": 320, "status": "delivered"},
    {"region": "Central", "packages": 10, "rate": 350, "status": "pending"}
]

blocked_regions = ["Mountain"]
total = sum(
    p["packages"] * p["rate"]
    for p in deliveries
    if p["region"] not in blocked_regions
    and p["status"] ==  "delivered"
    and ( p['region'] == 'Coastal' or p["packages"] >= 7)
    and not ( p["region"] == "Coastal"
             and p["packages"] < 5)
)

print(total)