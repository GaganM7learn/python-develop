orders = [
    {"item": "Desk", "amount": 8500},
    {"item": "Chair", "amount": 4500},
    {"item": "Laptop", "amount": 55000},
    {"item": "Printer", "amount": 12000},
    {"item": "Notebook", "amount": 800}
]

large_orders_total = sum(order["amount"] for order in orders if order["amount"] >=5000)
print(large_orders_total)