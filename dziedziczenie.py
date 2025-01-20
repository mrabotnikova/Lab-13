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
    
class Kurs:
    def __init__(self, nazwa_kursu, wykladowca):
        self.nazwa_kursu = nazwa_kursu
        self.wykladowca = wykladowca
        self.studenci = []

    def dodaj_studenta(self, student):
        self.studenci.append(student)

    def wyswietl_informacje(self):
        print(f"\nKurs: {self.nazwa_kursu}")
        print(f"Prowadzący: {self.wykladowca.imie} {self.wykladowca.nazwisko}")
        print("Studenci zapisani na kurs:")
        for student in self.studenci:
            print(f"- {student.imie} {student.nazwisko} (Indeks: {student.numer_indeksu})")


if __name__ == "__main__":
    student = Student("Jan", "Kowalski", "12345")
    wykladowca = Wykładowca("Anna", "Nowak", "Matematyka")
    student1 = Student("Jan", "Kowalski", "12345")
    student2 = Student("Maria", "Wiśniewska", "67890")
    wykladowca = Wykładowca("Anna", "Nowak", "Matematyka")

    kurs = Kurs("Analiza Matematyczna", wykladowca)
    kurs.dodaj_studenta(student1)
    kurs.dodaj_studenta(student2)

    kurs.wyswietl_informacje()


    print(student.przedstaw_sie())
    print(wykladowca.przedstaw_sie())





