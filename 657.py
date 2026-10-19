projects = [
    {"name": "Alpha", "team": "Development", "hours": 40, "rate": 1500, "status": "approved"},
    {"name": "Beta", "team": "Design", "hours": 25, "rate": 1200, "status": "approved"},
    {"name": "Gamma", "team": "Support", "hours": 50, "rate": 800, "status": "rejected"},
    {"name": "Delta", "team": "Development", "hours": 20, "rate": 1500, "status": "approved"},
    {"name": "Epsilon", "team": "Design", "hours": 35, "rate": 1200, "status": "approved"}
]

blocked_teams = ["Support"]

total_payment = sum(
    project['hours'] * project["rate"]
    for project in projects
    if project['team'] not in blocked_teams
    and project["status"] == "approved"
    and (
        project['team'] == "Development"
        or project['hours'] >= 30
    )
)
print(total_payment)