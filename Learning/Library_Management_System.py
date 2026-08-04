class Library:
    def __init__(self):
        self.No_of_Books = 0
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        self.No_of_Books += 1
        
    def showInfo(self):
        print(f"The library has {self.No_of_Books} books. The books are: ")
        for book in self.books:
            print(f"- {book}")
    
    def book_check(self):
        if self.No_of_Books == len(self.books):
            print("The number of books matches the list.")
        else:
            print("The number of books does not match the list.")
            
l1 = Library()
l1.add_book("Harry Potter")
l1.add_book("The Great Gatsby")
l1.add_book("To Kill a Mockingbird")
l1.showInfo()
l1.book_check()

l2 = Library()
l2.add_book("Pother panchali")
l2.add_book("Feluda somogro")
l2.showInfo()
l2.book_check()
