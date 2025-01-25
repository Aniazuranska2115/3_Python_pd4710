czy_sekwencja_dna_nieaktywna = True
czy_mutacja_punktowa = False
czy_nastapila_mutacja = True
czy_sa_unikalne_aminokwasy = False


sekcja_dna = "GTACCCTGA"
wynik = bool(sekcja_dna) # Zwróci True, ponieważ 'sekcja_dna' ma zawartość
print(f"czy cos znajduje sie w tej sekwencji {wynik}") # Wynik: True
pusta_sekwencja = ""
wynik_pusty = bool(pusta_sekwencja) # Zwróci False, ponieważ 'pusta_sekwencja' jest pustym ciągiem znaków
print(f"czy cos znajduje sie w tej sekwencji {wynik_pusty}") # Wynik: False

liczba_mutacji_1 = 0
liczba_mutacji_2 = 15
liczba_mutacji_3 = 7777

print(f"czy odbyły się mutacje {bool(liczba_mutacji_1)}") # false
print(f"czy odbyły się mutacje {bool(liczba_mutacji_2)}") # true
print(f"czy odbyły się mutacje {bool(liczba_mutacji_3)}") # true

pusta_sekwencja_2 = 0
print(f"czy cos znajduje sie w tej sekwencji {bool(pusta_sekwencja_2)}") # Zwróci False, ponieważ 'pusta_sekwencja_2' jest 0


pusta_lista_1 = []
print(f"czy cos znajduje sie w tej liście {bool(pusta_lista_1)}") # Wynik: False

pusta_lista_2 = [1,2,3,4,5]
print(f"czy cos znajduje sie w tej liście {bool(pusta_lista_2)}") # Wynik: True

liczba_mutacji = 100
liczba_mutacji += 50
liczba_mutacji += 65
liczba_mutacji *= 5
liczba_mutacji += 100
liczba_mutacji += 854

print(f"ilość mutacji {liczba_mutacji}")

ilosc_probek_dna = 20
ilosc_probek_dna -= 2
ilosc_probek_dna -= 3
ilosc_probek_dna -= 1
ilosc_probek_dna -= 5

print(f"aktualna ilość próbek DNA: {ilosc_probek_dna}")

liczba_nukleotydow = 1024
liczba_kodonow = liczba_nukleotydow // 127
reszta_nukleotydow = liczba_nukleotydow % 127
print(f"Z {liczba_nukleotydow} nukleotydów można utworzyć {liczba_kodonow} pełnych kodonów.")
print(f"Pozostaje {reszta_nukleotydow} nukleotydów.")

liczba_nukleotydow = 547782
liczba_kodonow = liczba_nukleotydow // 742
reszta_nukleotydow = liczba_nukleotydow % 742
print(f"Z {liczba_nukleotydow} nukleotydów można utworzyć {liczba_kodonow} pełnych kodonów.")
print(f"Pozostaje {reszta_nukleotydow} nukleotydów.")

sekwencja_1 = "ATCG"
sekwencja_2 = "GTCA"
sekwencja_3 = "GGGTAC"
sekwencja_4 = sekwencja_3
sekwencja_5 = "GTCA"

print(f"czy sekwencja 1 i 2 są takie same? {sekwencja_1 is sekwencja_2}") # "czy sekwencja 1 i 2 są takie same? False"
print(f"czy sekwencja 2 i 3 są takie same? {sekwencja_2 is sekwencja_3}") # "czy sekwencja 1 i 2 są takie same? False"
print(f"czy sekwencja 3 i 4 są takie same? {sekwencja_3 is sekwencja_4}") # "czy sekwencja 3 i 4 są takie same? True"
print(f"czy sekwencja 1 i 3 są takie same? {sekwencja_1 is sekwencja_3}") # "czy sekwencja 1 i 3 są takie same? False"
print(f"czy sekwencja 2 i 5 są takie same? {sekwencja_5 is sekwencja_2}") # "czy sekwencja 2 i 5 są takie same? True"

