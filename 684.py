repairs = [
    {"name": "R1", "type": "Phone", "cost": 12000, "discount": 1000, "status": "completed"},
    {"name": "R2", "type": "Laptop", "cost": 25000, "discount": 2000, "status": "completed"},
    {"name": "R3", "type": "Tablet", "cost": 8000, "discount": 500, "status": "pending"},
    {"name": "R4", "type": "Phone", "cost": 18000, "discount": 1500, "status": "completed"},
    {"name": "R5", "type": "Laptop", "cost": 9000, "discount": 500, "status": "completed"}
]

blocked_types = ["Tablet"]

total_revenue = sum(
    repair["cost"] - repair["discount"]
    for repair in repairs
    if repair["type"] not in blocked_types
    and repair["status"] == "completed"
    and (
        repair["type"] == "Laptop"
        or repair["cost"] >= 15000
    )
)

print(total_revenue)