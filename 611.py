orders = [
    {"item": "Laptop", "amount": 50000},
    {"item": "Phone", "amount": 30000},
    {"item": "Tablet", "amount": 20000}
]
total_amount = sum(order['amount'] for order in orders)

print(total_amount)