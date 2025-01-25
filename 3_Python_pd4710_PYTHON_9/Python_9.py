# Utworzenie zbioru i słownika
zbior_elementow = {'A', 'T', 'G', 'C'}
slownik_geny = {'BRCA1': 'Gen supresorowy nowotworów','TP53': 'Gen kontrolujący cykl komórkowy','MYC': 'Gen onkogenny'
}

# Dodanie nowego elementu do zbioru i pary klucz-wartość do słownika
zbior_elementow.add('U')  # Dodanie nowego elementu
slownik_geny['EGFR'] = 'Receptor czynnika wzrostu naskórka'  # klucz-wartość

# Sprawdzenie, czy element istnieje w zbiorze, a klucz w słowniku
element_do_sprawdzenia = 'A'
klucz_do_sprawdzenia = 'BRCA1'

# Sprawdzenie czy element istnieje w zbiorze
if element_do_sprawdzenia in zbior_elementow:
    print(f"Element '{element_do_sprawdzenia}' istnieje w zbiorze.")
else:
    print(f"Element '{element_do_sprawdzenia}' nie istnieje w zbiorze.")

# Sprawdzenie czy klucz istnieje w słowniku
if klucz_do_sprawdzenia in slownik_geny:
    print(f"Klucz '{klucz_do_sprawdzenia}' istnieje w słowniku.")
else:
    print(f"Klucz '{klucz_do_sprawdzenia}' nie istnieje w słowniku.")

# Usunięcie elementu ze zbioru
zbior_elementow.discard('G')
print(f"Zbiór po usunięciu elementu: {zbior_elementow}")

# Wyświetlenie zawartości słownika (klucze i wartości)
print("\nZawartość słownika:")
for klucz, wartosc in slownik_geny.items():
    print(f"{klucz}: {wartosc}")

# Sprawdzenie długości zbioru i wydruk odpowiedniego komunikatu
if len(zbior_elementow) > 3:
    print("\nZbiór zawiera więcej niż 3 elementy.")
else:
    print("\nZbiór zawiera 3 lub mniej elementów.")

# Sprawdzenie, czy określony klucz istnieje w słowniku i wydruk jego wartości
if klucz_do_sprawdzenia in slownik_geny:
    print(f"\nWartość klucza '{klucz_do_sprawdzenia}': {slownik_geny[klucz_do_sprawdzenia]}")
else:
    print(f"\nKlucz '{klucz_do_sprawdzenia}' nie istnieje w słowniku.")

# Operacja łączenia zbiorów
nowy_zbior = {'X', 'Y', 'Z'}
polaczony_zbior = zbior_elementow.union(nowy_zbior)
print(f"\nPołączony zbiór: {polaczony_zbior}")
