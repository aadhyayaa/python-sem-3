#write a program to create a simplified library management system using object oriented programming principles on python.
#this system should manage books and patrons(library users) applying for basic operations such as adding new books, registering patrons, 
#borrowing and returning books
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
###
library = Library()

book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures", "Alice Brown")

library.add_book(book1)
library.add_book(book2)

patron1 = Patron("Aadhya")
patron2 = Patron("Aradhya")

library.register_patron(patron1)
library.register_patron(patron2)
