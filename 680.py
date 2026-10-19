tickets = [
    {"name": "T1", "type": "VIP", "price": 5000, "status": "confirmed"},
    {"name": "T2", "type": "Regular", "price": 1500, "status": "confirmed"},
    {"name": "T3", "type": "Staff", "price": 3000, "status": "confirmed"},
    {"name": "T4", "type": "VIP", "price": 4500, "status": "pending"},
    {"name": "T5", "type": "Regular", "price": 2500, "status": "confirmed"},
    {"name": "T6", "type": "VIP", "price": 2000, "status": "confirmed"}
]

blocked_types = ["Staff"]

total_revenue = sum(
    ticket["price"]
    for ticket in tickets
    if ticket["type"] not in blocked_types
    and ticket["status"] == "confirmed"
    and (
        ticket["type"] == "VIP"
        or ticket["price"] >= 2000
    )
    and not (
        ticket["type"] == "Regular"
        and ticket["price"] < 2000
    )
)

print(total_revenue)