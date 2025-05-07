# Assignment:
# Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0 
    def __init__(self,name):
        self.name = name
        self.increment_book_count()

    @classmethod
    def increment_book_count(self):
        Book.total_books += 1



book = Book("CS")

print(book.total_books)

book2 = Book("DS")

print(book.total_books)