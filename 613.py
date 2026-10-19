orders = [
    {"item": "Laptop", "amount": 60000},
    {"item": "Mouse", "amount": 1500},
    {"item": "Monitor", "amount": 12000},
    {"item": "Keyboard", "amount": 2500}
]
large_orders = sum( order["amount"] for order in orders if order["amount"] >= 10000)

print(large_orders)