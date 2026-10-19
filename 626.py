payments = [
    {"customer": "Asha", "type": "Online", "amount": 2500, "status": "success"},
    {"customer": "Ravi", "type": "Cash", "amount": 1800, "status": "success"},
    {"customer": "Neha", "type": "Online", "amount": 4500, "status": "success"},
    {"customer": "Kiran", "type": "Online", "amount": 1200, "status": "failed"},
    {"customer": "Vijay", "type": "Cash", "amount": 5200, "status": "success"},
    {"customer": "Pooja", "type": "Online", "amount": 3800, "status": "success"}
]

total_online = sum( payment["amount"]
                   for payment in payments
                   if(payment["type"] == "Online" and payment["status"] == "success") and payment["amount"] >= 2000 )

print(total_online)