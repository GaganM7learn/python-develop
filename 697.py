deliveries = [
    {"zone": "West", "cost": 9000, "status": "delivered"},
    {"zone": "Central", "cost": 14000, "status": "delivered"},
    {"zone": "West", "cost": 4000, "status": "delivered"},
    {"zone": "North", "cost": 17000, "status": "delivered"},
    {"zone": "Central", "cost": 11000, "status": "pending"},
    {"zone": "South", "cost": 20000, "status": "delivered"}
]

blocked_zones = ["South"]



total = sum(
    p["cost"]
    for p in deliveries
    if p["zone"] not in blocked_zones
    and not ( p["status"] == "delivered")
    and ( p["zone"] == "West" 
         or p["cost"] <= 13000)
    and not ( p["zone"] == "West" and p["cost"] < 6000)
)

print(total)