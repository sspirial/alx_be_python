class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', '{self.file_size}')"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(book)

if __name__ == "__main__":
    library = Library()
    b1 = Book("Pride and Prejudice", "Jane Austen")
    b2 = EBook("Snow Crash", "Neal Stephenson", "500KB")  # <-- Bug fixed here
    b3 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    library.list_books()
    del b1
    del b2