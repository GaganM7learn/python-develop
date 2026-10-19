orders = [
    {"name": "Order A", "type": "Online", "amount": 12000, "status": "paid"},
    {"name": "Order B", "type": "Store", "amount": 8000, "status": "paid"},
    {"name": "Order C", "type": "Online", "amount": 5000, "status": "pending"},
    {"name": "Order D", "type": "Store", "amount": 15000, "status": "paid"}
]

blocked_types = ["Store"]

total = sum(
    order["amount"]
    for order in orders
    if order["type"] not in blocked_types
    and order["status"] == "paid"
    and order["amount"] >= 10000
)

print(total)