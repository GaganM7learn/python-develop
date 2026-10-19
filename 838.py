class Movie:
    def __init__(self, title, year):
        self.title = title
        self.author = year

    def __str__(self):
        return f"{self.title} by {self.year}"

movie =Movie("inception" , "(2010)" )
print(movie)