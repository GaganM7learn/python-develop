returns = [
    {"name": "Return A", "category": "Appliances", "amount": 18000, "fee": 800, "status": "approved"},
    {"name": "Return B", "category": "Books", "amount": 4000, "fee": 150, "status": "approved"},
    {"name": "Return C", "category": "Groceries", "amount": 12000, "fee": 300, "status": "approved"},
    {"name": "Return D", "category": "Appliances", "amount": 7000, "fee": 250, "status": "pending"},
    {"name": "Return E", "category": "Furniture", "amount": 14000, "fee": 600, "status": "approved"},
    {"name": "Return F", "category": "Books", "amount": 11000, "fee": 400, "status": "approved"}
]

blocked_categories = ["Groceries"]

total_return = sum(
    returnes["amount"] - returnes['fee']
    for returnes in returns
    if returnes['category'] not in blocked_categories
    and returnes["status"] == "approved"
    and (
        returnes['category'] == "Books" 
        or returnes['amount'] >= 13000
    )
)

print(total_return)