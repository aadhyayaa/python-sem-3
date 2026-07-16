#write a program to create a simplified library management system using object oriented programming principles on python.
#this system should manage books and patrons(library users) applying for basic operations such as adding new books, registering patrons, 
#borrowing and returning books

class book:
    def __init__(self, title, author):
        self.author=author
        self.title=title
class patron:
    def __init__(self,name):
        self.name=name
        
class library:
    def __init__(self):
        self.book=[]
        self.patron=[]

        def add_book(self,book):
            self.books.append(book)
            print(book.title, "added successfully")
            
            def register_patron(self,patron):
                self.patrons.append(patron)
                print(patron name,"registered succesfully")
                
                def


