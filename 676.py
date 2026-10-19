invoices = [
    {"name": "A", "department": "IT", "amount": 18000, "status": "paid"},
    {"name": "B", "department": "Sales", "amount": 25000, "status": "paid"},
    {"name": "C", "department": "HR", "amount": 12000, "status": "paid"},
    {"name": "D", "department": "IT", "amount": 9000, "status": "pending"},
    {"name": "E", "department": "Marketing", "amount": 22000, "status": "paid"},
    {"name": "F", "department": "IT", "amount": 14000, "status": "paid"}
]

blocked_departments = ["HR"]

total_amount = sum(
    invoice["amount"]
    for invoice in invoices
    if invoice["department"] not in blocked_departments
    and invoice["status"] == "paid"
    and (
        invoice["department"] == "IT"
        or invoice["amount"] >= 20000
    )
    and not (
        invoice["department"] == "IT"
        and invoice["amount"] < 15000
    )
)

print(total_amount)