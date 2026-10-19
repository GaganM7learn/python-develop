shipments = [
    {"region": "Coastal", "packages": 8, "rate": 300, "status": "delivered"},
    {"region": "Mountain", "packages": 10, "rate": 450, "status": "delivered"},
    {"region": "Coastal", "packages": 4, "rate": 250, "status": "delivered"},
    {"region": "Central", "packages": 6, "rate": 350, "status": "delivered"}
]

blocked_regions = ["Mountain"]

total = sum(
    s["packages"] * s["rate"]
    for s in shipments
    if s["region"] not in blocked_regions
    and s["status"] == "delivered"
    and (
        s["region"] == "Coastal"
        or s["packages"] >= 6
    )
    and not (
        s["region"] == "Coastal"
        and s["packages"] < 5
    )
)

print(total)