sales = [
    {"product": "Laptop", "category": "Electronics", "amount": 75000, "status": "paid"},
    {"product": "Phone", "category": "Electronics", "amount": 45000, "status": "pending"},
    {"product": "Desk", "category": "Furniture", "amount": 18000, "status": "paid"},
    {"product": "Monitor", "category": "Electronics", "amount": 22000, "status": "paid"},
    {"product": "Chair", "category": "Furniture", "amount": 9000, "status": "paid"},
    {"product": "Tablet", "category": "Electronics", "amount": 30000, "status": "cancelled"}
]

total_electronics = sum( sale['amount']
                        for sale in sales 
                        if sale["category"] == "Electronics" and sale["status"] == "paid" )

print(total_electronics)