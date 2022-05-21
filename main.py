class Library(list):

    def __init__(self):
        super().__init__()

    def add_book(self, book):
        self.append(book)

    def print_get_count_books(self):
        result = sorted(set([(book.title, book.author, self.count(book)) for book in self]), key = lambda x: x[0])
        for book in result:
            print(book)


class Book:

    def __init__(self, title, author, year, reader = "NN"):
        self.title = title
        self.author = author
        self.year = year
        self.reader = reader

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

bib = Library()
n = int(input())

for i in range(n):
    line = eval(input())
    title = line[0]
    author = line[1]
    year = line[2]
    book = Book(title, author, year)
    bib.add_book(book)

bib.print_get_count_books()


