books = [
    {"title": "Python Basics", "price": 800, "pages": 350, "rating": 4.2},
    {"title": "Data Science", "price": 1200, "pages": 500, "rating": 4.7},
    {"title": "Web Development", "price": 950, "pages": 420, "rating": 4.5},
    {"title": "Machine Learning", "price": 1500, "pages": 600, "rating": 4.8},
    {"title": "Algorithms", "price": 1100, "pages": 550, "rating": 4.6}
]

best_book = max( (book for book in books if book["pages"] >= 500 and book["rating"] >= 4.6 ) , key=lambda book : book["price"] )
print(best_book)