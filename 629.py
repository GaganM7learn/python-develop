sales = [
    {"product": "Phone", "category": "Electronics", "amount": 45000, "status": "paid"},
    {"product": "Table", "category": "Furniture", "amount": 12000, "status": "paid"},
    {"product": "Laptop", "category": "Electronics", "amount": 70000, "status": "pending"},
    {"product": "Chair", "category": "Furniture", "amount": 8000, "status": "paid"},
    {"product": "Camera", "category": "Electronics", "amount": 35000, "status": "paid"}
]

total_selected = sum(
    sale["aamount"]
    for sale in sales
    if ( sale['category'] == "Electronics" or sale['category'] == "Furniture") and sale["status"] == 'paid'
)
print(total_selected)