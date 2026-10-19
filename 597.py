books = [
    {"title": "Python Basics", "pages": 320},
    {"title": "Data Science", "pages": 450},
    {"title": "Web Development", "pages": 280},
    {"title": "Machine Learning", "pages": 520}
]

sorted_table = sorted(books , key=lambda item : item["pages"] , reverse=True)
print(sorted_table)
