tasks = [
    {"name": "Website", "team": "Engineering", "hours": 45, "rate": 1800, "status": "approved"},
    {"name": "Logo", "team": "Creative", "hours": 20, "rate": 1000, "status": "approved"},
    {"name": "Helpdesk", "team": "Support", "hours": 50, "rate": 900, "status": "approved"},
    {"name": "Mobile App", "team": "Engineering", "hours": 25, "rate": 1800, "status": "pending"},
    {"name": "Campaign", "team": "Marketing", "hours": 35, "rate": 1300, "status": "approved"},
    {"name": "Database", "team": "Engineering", "hours": 15, "rate": 2000, "status": "approved"}
]

blocked_teams = ["Support"]
total_payment = sum(
    task["hours"] * task["rate"]
    for task in tasks
    if task["team"] not in blocked_teams
    and task["status"] == "approved"
    and(
        task["team"] == "Engineering"
        or task['hours'] >= 30

    )
)

print(total_payment)