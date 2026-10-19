
sales = [
    {"product": "Laptop", "category": "Electronics", "amount": 50000},
    {"product": "Sofa", "category": "Furniture", "amount": 30000},
    {"product": "Shirt", "category": "Clothing", "amount": 4000},
    {"product": "Phone", "category": "Electronics", "amount": 25000},
    {"product": "Table", "category": "Furniture", "amount": 12000}
]

blocked_categories= ["Fashion"]

total_purchases = sum(
    sale["amount"]
    for sale in sales
    if sale["category"] not in blocked_categories
    and ( sale['category'] == "Electronics" or sale["amount"] >= 20000 )
)
print(total_purchases)