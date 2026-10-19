transactions = [
    {"name": "Amazon", "amount": 6500, "status": "completed"},
    {"name": "Uber", "amount": 2200, "status": "failed"},
    {"name": "Flipkart", "amount": 4800, "status": "completed"},
    {"name": "Swiggy", "amount": 3500, "status": "cancelled"},
    {"name": "Myntra", "amount": 7200, "status": "completed"},
    {"name": "Zomato", "amount": 4100, "status": "failed"}
]

total_valid_transactions = sum(
    item["amount"]
    for item in transactions 
    if not item['status'] == "failed"
    and item["amount"] >= 4000
)

print(total_valid_transactions)