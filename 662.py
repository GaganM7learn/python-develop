refunds = [
    {"name": "Order A", "category": "Electronics", "amount": 12000, "fee": 500, "status": "approved"},
    {"name": "Order B", "category": "Clothing", "amount": 5000, "fee": 200, "status": "approved"},
    {"name": "Order C", "category": "Food", "amount": 3000, "fee": 100, "status": "rejected"},
    {"name": "Order D", "category": "Electronics", "amount": 8000, "fee": 300, "status": "approved"},
    {"name": "Order E", "category": "Home", "amount": 15000, "fee": 700, "status": "approved"}
]

blocked_categories = ["Food"]

total_refund = sum(
    refund["amount"] - refund["fee"]
    for refund in refunds
    if refund["category"] not in blocked_categories
    and refund["status"] == "approved"
    and (
        refund["category"] == "Electronics"
        or refund["amount"] >= 10000
    )
)

print(total_refund)