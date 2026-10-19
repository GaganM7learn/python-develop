bills = [
    {"name": "Bill A", "department": "Engineering", "amount": 32000, "discount": 2500, "status": "paid"},
    {"name": "Bill B", "department": "Admin", "amount": 15000, "discount": 800, "status": "paid"},
    {"name": "Bill C", "department": "Marketing", "amount": 24000, "discount": 1200, "status": "pending"},
    {"name": "Bill D", "department": "Engineering", "amount": 11000, "discount": 500, "status": "paid"},
    {"name": "Bill E", "department": "Finance", "amount": 28000, "discount": 1800, "status": "paid"},
    {"name": "Bill F", "department": "Admin", "amount": 22000, "discount": 1000, "status": "paid"}
]

blocked_departments = ["Admin"]

total_bill_amount = sum(
    bill["amount"] - bill["discount"]
    for bill in bills
    if bill["department"] not in blocked_departments
    and bill["status"] == "paid"
    and (
        bill["department"] == "Engineering"
        or bill["amount"] >= 25000
    )
)

print(total_bill_amount)