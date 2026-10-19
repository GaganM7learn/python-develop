players = [
    {"name": "Arjun", "team": "Blue", "score": 82},
    {"name": "Neha", "team": "Red", "score": 91},
    {"name": "Vikram", "team": "Blue", "score": 74},
    {"name": "Priya", "team": "Red", "score": 85}
]

sorted_players = sorted( players , key=lambda player : (player["team"] , player["score"]))
print(sorted_players)