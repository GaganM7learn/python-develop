services = [
    {"name": "S1", "type": "Cleaning", "cost": 7000, "discount": 500, "status": "completed"},
    {"name": "S2", "type": "Installation", "cost": 18000, "discount": 1500, "status": "completed"},
    {"name": "S3", "type": "Consulting", "cost": 25000, "discount": 2000, "status": "completed"},
    {"name": "S4", "type": "Cleaning", "cost": 12000, "discount": 1000, "status": "pending"},
    {"name": "S5", "type": "Installation", "cost": 9000, "discount": 500, "status": "completed"},
    {"name": "S6", "type": "Consulting", "cost": 16000, "discount": 1000, "status": "completed"}
]

blocked_types = ["Consulting"]

total_revenue = sum(
    ser["cost"] - ser['discount']
    for ser in services
    if ser["type"] not in blocked_types
    and ser['status'] == "completed"
    and (
        ser["type"] == "Installation"
        or ser['cost'] >= 10000
    )
)

print(total_revenue)