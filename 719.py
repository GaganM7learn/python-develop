shipments = [
    {"region": "Central", "boxes": 6, "rate": 250, "status": "sent"},
    {"region": "Coastal", "boxes": 7, "rate": 300, "status": "sent"},
    {"region": "Central", "boxes": 3, "rate": 180, "status": "sent"},
    {"region": "Mountain", "boxes": 9, "rate": 420, "status": "sent"},
    {"region": "Coastal", "boxes": 10, "rate": 280, "status": "pending"}
]
blocked = ["Mountain"]

total = sum(
    p["boxes"]  * p["rate"]
    for p in shipments
    if p["region"] not in blocked
    and p["status"] == "sent"
    and (p["region"] == "Central" or p["boxes"] >= 7 )
    and not ( p["region"] == "Central" and p["boxes"] < 4 )  

)

print(total)