invoices = [
    {"name": "A", "category": "Electronics", "quantity": 3, "price": 10000, "status": "paid"},
    {"name": "B", "category": "Furniture", "quantity": 2, "price": 20000, "status": "paid"},
    {"name": "C", "category": "Fashion", "quantity": 5, "price": 3000, "status": "paid"},
    {"name": "D", "category": "Electronics", "quantity": 1, "price": 25000, "status": "pending"},
    {"name": "E", "category": "Furniture", "quantity": 4, "price": 8000, "status": "paid"}
]

blocked_categories = ["Fashion"]
total_invoice_value = sum(
    invoice["quantity"] * invoice["price"]
    for invoice in invoices
    if invoice["category"] not in blocked_categories
    and (
        invoice["category"] == "Electronics"
        or invoice["quantity"] >= 4
    )
    and invoice['status'] =="paid"
)

print(total_invoice_value)