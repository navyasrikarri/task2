class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        else:
            return False

    def return_book(self):
        self.is_borrowed = False

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_borrowed = []

    def borrow_book(self, book):
        if book and book.borrow():
            self.books_borrowed.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.books_borrowed:
            book.return_book()
            self.books_borrowed.remove(book)
            return True
        return False

    def get_borrowed_books(self):
        return [book.title for book in self.books_borrowed]

class Library:
    def __init__(self, name):
        self.name = name
        self.catalog = []
        self.members = []

    def add_book(self, book):
        self.catalog.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_id, isbn):
        book = self.find_book_by_isbn(isbn)
        member = self.find_member_by_id(member_id)
        return member.borrow_book(book) if book and member else False

    def return_book(self, member_id, isbn):
        book = self.find_book_by_isbn(isbn)
        member = self.find_member_by_id(member_id)
        return member.return_book(book) if book and member else False

    def find_book_by_isbn(self, isbn):
        for book in self.catalog:
            if book.isbn == isbn and not book.is_borrowed:
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def list_available_books(self):
        return [book.title for book in self.catalog if not book.is_borrowed]

library = Library("Central Library")

library.add_book(Book("1984", "George Orwell", "9780451524935"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "9780060935467"))

member1 = Member("Alice Smith", "M001")
member2 = Member("Bob Jones", "M002")
library.add_member(member1)
library.add_member(member2)

print(library.borrow_book("M001", "9780451524935"))
print(library.borrow_book("M002", "9780060935467"))  

print(library.list_available_books())

print(member1.return_book(library.find_book_by_isbn("9780451524935")))
