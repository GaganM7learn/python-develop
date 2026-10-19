bookings = [
    {"property": "Apartment A", "type": "Residential", "days": 20, "rate": 1800, "status": "paid"},
    {"property": "Store B", "type": "Commercial", "days": 28, "rate": 2200, "status": "paid"},
    {"property": "Cabin C", "type": "Vacation", "days": 12, "rate": 3500, "status": "paid"},
    {"property": "Office D", "type": "Commercial", "days": 18, "rate": 2600, "status": "pending"},
    {"property": "House E", "type": "Residential", "days": 10, "rate": 2000, "status": "paid"},
    {"property": "Mall F", "type": "Commercial", "days": 30, "rate": 3000, "status": "paid"}
]

blocked_types = ["Vacation"]

total_booking_income = sum(
    book["days"] * book["rate"]
    for book in bookings
    if book["type"] not in blocked_types

    and book['status'] == "paid"
    and ( book["type"] == "Residential" or book["days"] >= 25 )
)

print(total_booking_income)