import os
from datetime import datetime
from biologia import opis_komorki, licz_nukleotydy

def main():
    print(opis_komorki())

    katalog = "dane_bio"
    if not os.path.exists(katalog):
        os.makedirs(katalog)
        print(f"Utworzono katalog: {katalog}")

    sekwencja = "AGCTTAGCTAAGGCT"

    wyniki = licz_nukleotydy(sekwencja)

    sciezka_pliku = os.path.join(katalog, "nukleotydy.txt")

    with open(sciezka_pliku, "w") as plik:
        plik.write("Wyniki liczenia nukleotydów:\n")
        for nukleotyd, liczba in wyniki.items():
            plik.write(f"{nukleotyd}: {liczba}\n")

        aktualny_czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        plik.write(f"\nData i czas utworzenia pliku: {aktualny_czas}\n")

    print(f"Wyniki zapisano w pliku: {sciezka_pliku}")

if __name__ == "__main__":
    main()