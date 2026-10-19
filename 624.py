transactions = [
    {"id": 101, "category": "Food", "amount": 850, "status": "completed"},
    {"id": 102, "category": "Travel", "amount": 3200, "status": "completed"},
    {"id": 103, "category": "Food", "amount": 1200, "status": "pending"},
    {"id": 104, "category": "Shopping", "amount": 4500, "status": "completed"},
    {"id": 105, "category": "Travel", "amount": 2800, "status": "cancelled"},
    {"id": 106, "category": "Food", "amount": 950, "status": "completed"}
]

total_food = sum( 
    okay['amount']
    for okay in transactions 
    if okay["category"] == "Food"  and okay["status"] == "completed"
)
print(total_food)