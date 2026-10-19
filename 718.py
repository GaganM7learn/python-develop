shipments = [
    {"region": "North", "boxes": 5, "rate": 200, "status": "sent"},
    {"region": "South", "boxes": 8, "rate": 300, "status": "sent"},
    {"region": "East", "boxes": 2, "rate": 150, "status": "sent"},
    {"region": "West", "boxes": 10, "rate": 400, "status": "pending"}
]

blocked = ["East"]

total = sum(
    s["boxes"] * s["rate"]
    for s in shipments
    if s["region"] not in blocked
    and s["status"] == "sent"
    and (s["region"] == "North" or s["boxes"] >= 8)
)

print(total)  # 3400