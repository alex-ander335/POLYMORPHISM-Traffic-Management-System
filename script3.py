class Book:
    #class variable: tracks total books created
    total_books =0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.total_books = Book.total_books += 1

    def display_infor(self):
        print(f'Title: {self.title}, Author: {self.author}')
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    @staticmethod
    def is_valid_isdb(isdn):
        return isinstance(isdn, str) and
isdn.isdigit()and len(isbn) ==13



