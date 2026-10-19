orders = [
    {"item": "Laptop", "quantity": 2, "price": 60000, "status": "delivered"},
    {"item": "Mouse", "quantity": 5, "price": 1200, "status": "delivered"},
    {"item": "Keyboard", "quantity": 3, "price": 2500, "status": "pending"},
    {"item": "Monitor", "quantity": 2, "price": 18000, "status": "delivered"},
    {"item": "Headphones", "quantity": 4, "price": 3500, "status": "cancelled"},
    {"item": "Webcam", "quantity": 3, "price": 2800, "status": "delivered"}
]

order_value = sum(
    order["quantity"] * order['price']
    for order in orders 
    if (order["status"] == "delivered" and order['quantity'] >= 2 ) and order['price'] >= 5000 )
print(order_value)