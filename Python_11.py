# Definicja klasy Organizm
class Organizm:
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj

    def opisz(self):
        return f"Organizm: {self.nazwa}, Rodzaj: {self.rodzaj}"

    @staticmethod
    def transkrybuj(sekwencja_dna):
        return sekwencja_dna.replace("T", "U")


# Definicja klasy Bakteria dziedziczącej po klasie Organizm
class Bakteria(Organizm):
    def __init__(self, nazwa, rodzaj, kształt):
        super().__init__(nazwa, rodzaj)  # Wywołanie konstruktora klasy bazowej
        self.kształt = kształt

    def opisz(self):
        opis_organizm = super().opisz()  # Wywołanie metody opisz z klasy Organizm
        return f"{opis_organizm}, Kształt: {self.kształt}"


# Główna część programu
if __name__ == "__main__":
    # Tworzenie instancji klasy Bakteria
    bakteria1 = Bakteria("Escherichia coli", "Gram-ujemna", "Pałeczkowaty")
    bakteria2 = Bakteria("Staphylococcus aureus", "Gram-dodatnia", "Kulisty")

    # Wywołanie metody opisz dla instancji
    print(bakteria1.opisz())
    print(bakteria2.opisz())

    # Testowanie metody statycznej transkrybuj
    dna_sekwencja = "ATGCGTACGTAG"
    rna_sekwencja = Organizm.transkrybuj(dna_sekwencja)
    print(f"\nSekwencja DNA: {dna_sekwencja}")
    print(f"Sekwencja RNA: {rna_sekwencja}")
