sales = [
    {"category": "Food", "amount": 1000},
    {"category": "Travel", "amount": 2000},
    {"category": "Food", "amount": 1500}
]
blocked = ["Travel"]

total = sum(
    sale["amount"]
    for sale in sales
    if sale["category"] not in blocked
)

print(total)