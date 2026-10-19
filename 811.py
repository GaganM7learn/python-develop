class Book :
    def __init__(self  , title , pages) :
        self.title = title
        self.pages = pages

book = Book("Dune" , 500 )

print(book.title)
print(book.pages)