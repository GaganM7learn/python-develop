orders = [
    {"item": "Keyboard", "type": "Online", "amount": 7000, "status": "completed"},
    {"item": "Mouse", "type": "Cash", "amount": 4000, "status": "completed"},
    {"item": "Monitor", "type": "Card", "amount": 18000, "status": "pending"},
    {"item": "Printer", "type": "Online", "amount": 22000, "status": "completed"},
    {"item": "Speaker", "type": "UPI", "amount": 6000, "status": "completed"},
    {"item": "Webcam", "type": "Cash", "amount": 12000, "status": "completed"}
]

blocked_types = ["Cash", "UPI"]

total = sum(
    item["amount"]
    for item in orders
    if item["type"] not in blocked_types
    and item["status"] == "completed"
    and item["amount"] >= 7000
)

print(total)