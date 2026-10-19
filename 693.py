orders = [
    {"amount": 500, "status": "paid"},
    {"amount": 800, "status": "pending"},
    {"amount": 1200, "status": "paid"}
]
total = sum( order["amount"]
            for order in orders 
            if order["status"] == "paid"
            
)

print(total)