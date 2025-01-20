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

class Wykładowca(Osoba):
    def __init__(self, imie, nazwisko, przedmiot):
        super().__init__(imie, nazwisko)
        self.przedmiot = przedmiot

    def przedstaw_sie(self):
        return f"Jestem wykładowcą. {super().przedstaw_sie()} Prowadzę zajęcia z {self.przedmiot}."

if __name__ == "__main__":
    student = Student("Jan", "Kowalski", "12345")
    wykladowca = Wykładowca("Anna", "Nowak", "Matematyka")

    print(student.przedstaw_sie())
    print(wykladowca.przedstaw_sie())



