invoices = [
    {"name": "Invoice A", "department": "IT", "amount": 25000, "discount": 2000, "status": "paid"},
    {"name": "Invoice B", "department": "HR", "amount": 12000, "discount": 500, "status": "paid"},
    {"name": "Invoice C", "department": "Sales", "amount": 18000, "discount": 1000, "status": "pending"},
    {"name": "Invoice D", "department": "IT", "amount": 9000, "discount": 300, "status": "paid"},
    {"name": "Invoice E", "department": "Finance", "amount": 30000, "discount": 2500, "status": "paid"}
]

blocked_departments = ["HR"]

total_invoice = sum(
    invoice["amount"] - invoice["discount"]
    for invoice in invoices
    if invoice["department"] not in blocked_departments
    and invoice["status"] == "paid"
    and (
        invoice['department'] == "IT"
        or invoice["amount"] >= 20000
    )
)

print(total_invoice)