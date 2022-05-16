class Biblioteka:

    def __init__(self, lista_ksiazek = [], egzemplarze = []):
        self.lista_ksiazek = lista_ksiazek
        self.egzemplarze = egzemplarze

    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok):
        k1 = Ksiazka(tytul, autor)
        if k1 not in self.lista_ksiazek:
            self.lista_ksiazek.append(k1)
        e1 = Egzemplarz(rok_wydania=rok, tytul=tytul, autor=autor)
        self.egzemplarze.append(e1)
        for ksiazka in self.lista_ksiazek:
            if ksiazka == k1:
                ksiazka.ile += 1

    def wypisz_ksiazki(self):
        for e in self.lista_ksiazek:
            wynik = (e.tytul, e.autor, self.egzemplarze.count(e))
            print(wynik)

class Ksiazka:

    def __init__(self, tytul, autor, ile = 0):
        self.tytul = tytul
        self.autor = autor
        self.ile = ile

    def __eq__(self, other):
        if isinstance(other, Ksiazka):
            return self.tytul == other.tytul and self.autor == other.autor
        return False

class Egzemplarz(Ksiazka):

    def __init__(self, rok_wydania, tytul, autor, wypozyczony=False):
        super().__init__(tytul, autor)
        self.rok_wydania = rok_wydania
        self.wypozyczony = wypozyczony


ile = int(input())
for i in range(ile):
    query = eval(input())

    bib = Biblioteka()
    bib.dodaj_egzemplarz_ksiazki(query[0], query[1], query[2])

bib.wypisz_ksiazki()


