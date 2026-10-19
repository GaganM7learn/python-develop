shipments = [
    {"zone": "North", "cost": 8000, "status": "delivered"},
    {"zone": "South", "cost": 12000, "status": "delivered"},
    {"zone": "North", "cost": 5000, "status": "pending"},
    {"zone": "East", "cost": 18000, "status": "delivered"}
]

blocked_zones = ["East"]

total = sum(
    s["cost"]
    for s in shipments
    if s["zone"] not in blocked_zones
    and s["status"] == "delivered"
    and (
        s["zone"] == "North"
        or s["cost"] >= 10000
    )
    and not (
        s["zone"] == "North"
        and s["cost"] < 7000
    )
)

print(total)