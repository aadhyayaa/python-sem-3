class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title
class Patron:
    def __init__(self, name):
        self.name = name
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(book.title, "added successfully")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(patron.name, "registered successfully")
        
#####

library = Library()

book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures", "Alice Brown")

library.add_book(book1)
library.add_book(book2)

patron1 = Patron("aadhya")
patron2 = Patron("aradhya")

library.register_patron(patron1)
library.register_patron(patron2)