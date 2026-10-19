movies = [
    {"title": "Interstellar", "rating": 8.6},
    {"title": "Avatar", "rating": 7.8},
    {"title": "Gladiator", "rating": 8.5},
    {"title": "Titanic", "rating": 7.9}
]

sorted_movies = sorted( movies , key=lambda item : item["title"])

print(sorted_movies)