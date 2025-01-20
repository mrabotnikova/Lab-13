class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return f"Nazywam się {self.imie} {self.nazwisko}."


class Student(Osoba):
    def __init__(self, imie, nazwisko, numer_indeksu):
        super().__init__(imie, nazwisko)
        self.numer_indeksu = numer_indeksu

    def przedstaw_sie(self):
        return f"Jestem studentem. {super().przedstaw_sie()} Mój numer indeksu to {self.numer_indeksu}."

