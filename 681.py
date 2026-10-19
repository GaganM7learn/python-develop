

subscriptions = [
    {"name": "S1", "plan": "Premium", "price": 6000, "status": "active"},
    {"name": "S2", "plan": "Basic", "price": 1200, "status": "active"},
    {"name": "S3", "plan": "Trial", "price": 500, "status": "active"},
    {"name": "S4", "plan": "Premium", "price": 4500, "status": "cancelled"},
    {"name": "S5", "plan": "Basic", "price": 2500, "status": "active"},
    {"name": "S6", "plan": "Premium", "price": 3000, "status": "active"},
    {"name": "S7", "plan": "Basic", "price": 1800, "status": "active"}
]

blocked_plans = ["Trial"]


total_revenue = sum(
    sub["price"]
    for sub in subscriptions
    if sub["plan"] not in blocked_plans

    and sub["status"] == "active"
    and (
        sub["plan"] == "Premium"
        or sub["price"] >= 2000
    )
    and not (
        sub["plan"] == "Basic"
        and sub['price'] < 2000
    )
)
print(total_revenue)