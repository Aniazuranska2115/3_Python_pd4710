# Funkcja opisująca białko
def charakterystyka_białka(sekwencja, masa, pI):
    return f"Białko: sekwencja '{sekwencja}', masa {masa} Da, punkt izoelektryczny {pI}."

# Funkcja obliczająca sumę mas i średni punkt izoelektryczny
def sumuj_cechy_bialek(**kwargs):
    suma_mas = 0
    suma_pI = 0
    liczba_bialek = len(kwargs) // 2  # Zakładamy pary masa/pI

    # Iteracja przez argumenty
    for klucz, wartosc in kwargs.items():
        if "masa" in klucz:
            suma_mas += wartosc
        elif "pI" in klucz:
            suma_pI += wartosc

    # Oblicz średni punkt izoelektryczny
    if liczba_bialek > 0:
        srednia_pI = suma_pI / liczba_bialek
    else:
        srednia_pI = 0

    return suma_mas, srednia_pI

# Główna część programu
if __name__ == "__main__":
    # Przykładowe dane dla białek
    masa1, pI1 = 50000.0, 6.5
    masa2, pI2 = 30000.0, 5.8

    # Opis białek
    print(charakterystyka_białka("AAAAA", masa1, pI1))
    print(charakterystyka_białka("BBBBB", masa2, pI2))

    # Suma mas i średni punkt izoelektryczny
    suma_mas, srednia_pI = sumuj_cechy_bialek(masa1=masa1, pI1=pI1, masa2=masa2, pI2=pI2)
    print(f"\nSuma mas białek: {suma_mas} Da")
    print(f"Średni punkt izoelektryczny: {srednia_pI}")

