orders = [
    {"item": "Keyboard", "amount": 2500},
    {"item": "Mouse", "amount": 1200},
    {"item": "Monitor", "amount": 15000},
    {"item": "Webcam", "amount": 3500}
]

total_order_amount = sum( order["amount"] for order in orders )

print(total_order_amount)