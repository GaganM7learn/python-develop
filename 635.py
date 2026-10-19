payments = [
    {"customer": "Asha", "amount": 5000, "status": "success"},
    {"customer": "Ravi", "amount": 3000, "status": "failed"},
    {"customer": "Neha", "amount": 7000, "status": "success"},
    {"customer": "Kiran", "amount": 2500, "status": "cancelled"},
    {"customer": "Vijay", "amount": 4500, "status": "success"}
]

total_valid_payment = sum(
    payment["amount"]
    for payment in payments
    if not payment["status"] == "failed"
    and payment["amount"] >= 4000
)

print(total_valid_payment)