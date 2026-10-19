rentals = [
    {"property": "Flat A", "type": "Residential", "days": 30, "rate": 1500, "status": "paid"},
    {"property": "Shop B", "type": "Commercial", "days": 20, "rate": 2500, "status": "paid"},
    {"property": "Flat C", "type": "Residential", "days": 15, "rate": 1200, "status": "pending"},
    {"property": "Office D", "type": "Commercial", "days": 25, "rate": 2000, "status": "paid"},
    {"property": "Villa E", "type": "Vacation", "days": 10, "rate": 4000, "status": "paid"}
]

blocked_types = ["Vacation"]
total_rent = sum(
    rental["days"] * rental['rate']
    for rental in rentals
    if rental["type"] not in blocked_types
    and rental['status'] == "paid"
    and (
        rental['type'] =="Residential"
        or rental['days'] >= 25
    )
)
print(total_rent)
