movies = [
    {"title": "Inception", "rating": 8.8, "duration": 148, "price": 300},
    {"title": "Interstellar", "rating": 8.7, "duration": 169, "price": 350},
    {"title": "The Matrix", "rating": 8.7, "duration": 136, "price": 250},
    {"title": "Gladiator", "rating": 8.5, "duration": 155, "price": 280},
    {"title": "Parasite", "rating": 8.5, "duration": 132, "price": 220}
]

cheapest_movies = min( (movie for movie in movies if movie["rating"] >= 8.5 and movie["duration" >= 140] ) , key=lambda movie : movie["price"] )

print(cheapest_movies)