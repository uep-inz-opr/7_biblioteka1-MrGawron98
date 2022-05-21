class Library(list):

    def __init__(self):
        super(Library, self).__init__()

    def add_book(self, author, title, year, state = "wolny"):
        self.append({"author": author, "title": title, "year": year, "state": state, "reader": "NN"})

    def get_uniques(self):
        return list(set([(book['title'], book['author']) for book in self]))

    def get_uniques_count(self):
        uniques = self.get_uniques()
        result = []
        for book in uniques:
            count = []
            for e in self:
                if e['title'] == book[0] and e['author'] == book[1]:
                    count.append(e)
            result.append((book[0], book[1], len(count)))
        return sorted(result, key = lambda x: x[0])

bib = Library()

n = int(input())

for i in range(n):
    book = eval(input())
    title = book[0]
    author = book[1]
    year = book[2]
    bib.add_book(author, title, year)

for book in bib.get_uniques_count():
    print(book)

    # def __init__(self):
    #     self.core = dict()
    #
    # def add_book(self, author, title, year, state = "wolny", reader = "NN"):
    #     #if author not in self.core:
    #     #    self.core[author] = []
    #     self.core[author].append({"title":title, "year":year, "state":state, "reader":reader})
    #
    # def get_size(self):
    #     count = 0
    #     for author in self.core:
    #             count += len(self.core[author])
    #     return count
    #
    # def get_library(self):
    #     list = []
    #     for author in self.core:
    #         for book in self.core[author]:
    #             book["author"] = author
    #             list.append(book)
    #     return list
    #
    # def get_count_books(self):
    #     uniques = []
    #     for book in self.get_library():
    #         uniques.append((book['title'], book['author']))
    #     uniques_set = set(uniques)
    #     result = []
    #     for book in uniques_set:
    #         i = uniques.count(book)
    #         result.append((book[0], book[1], i))
    #     result = sorted(result, key = lambda x: x[0])
    #     for x in result:
    #         print(x)

# class Biblioteka:
#
#     def __init__(self, lista_ksiazek = [], egzemplarze = []):
#         self.lista_ksiazek = lista_ksiazek
#         self.egzemplarze = egzemplarze
#
#     def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok):
#         k1 = Ksiazka(tytul, autor)
#         if k1 not in self.lista_ksiazek:
#             self.lista_ksiazek.append(k1)
#         e1 = Egzemplarz(rok_wydania=rok, tytul=tytul, autor=autor)
#         self.egzemplarze.append(e1)
#         for ksiazka in self.lista_ksiazek:
#             if ksiazka == k1:
#                 ksiazka.ile += 1
#
#     def wypisz_ksiazki(self):
#         result = []
#         for e in self.lista_ksiazek:
#             wynik = (e.tytul, e.autor, self.egzemplarze.count(e))
#             result.append(wynik)
#
#         result = sorted(result, key = lambda x: x[0])
#         for r in result: print(r)
#
#
# class Ksiazka:
#
#     def __init__(self, tytul, autor, ile = 0):
#         self.tytul = tytul
#         self.autor = autor
#         self.ile = ile
#
#     def __eq__(self, other):
#         if isinstance(other, Ksiazka):
#             return self.tytul == other.tytul and self.autor == other.autor
#         return False
#
# class Egzemplarz(Ksiazka):
#
#     def __init__(self, rok_wydania, tytul, autor, wypozyczony=False):
#         super().__init__(tytul, autor)
#         self.rok_wydania = rok_wydania
#         self.wypozyczony = wypozyczony
#
#
# ile = int(input())
# for i in range(ile):
#     query = eval(input())
#
#     bib = Biblioteka()
#     bib.dodaj_egzemplarz_ksiazki(query[0], query[1], query[2])
#
# bib.wypisz_ksiazki()
#
#
