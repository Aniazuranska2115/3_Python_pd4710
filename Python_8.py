lista_zasad_azotowych = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'G']
krotka_zasady_azotowe = ('Adenina', 'Tymina', 'Cytozyna', 'Guanina')

# wydruk pierwszego i ostatniego elementu listy oraz krotki
print("Pierwszy element listy:", lista_zasad_azotowych[0])
print("Ostatni element listy:", lista_zasad_azotowych[-1])
print("Pierwszy element krotki:", krotka_zasady_azotowe[0])
print("Ostatni element krotki:", krotka_zasady_azotowe[-1])

# Modyfikacja elementu listy
lista_zasad_azotowych[2] = 'C'
print("Zmieniona lista:", lista_zasad_azotowych)
# dodanie elementu do listy
lista_zasad_azotowych.append('T')
print("Lista po dodaniu elementu:", lista_zasad_azotowych)

# iteracja przez elementy listy i krotki
print("\nElementy listy:")
for element in lista_zasad_azotowych:
    print(element)

print("\nElementy krotki:")
for element in krotka_zasady_azotowe:
    print(element)

# utworzenie nowej listy za pomocą list comprehension
lista_male_litery = [litera.lower() for litera in lista_zasad_azotowych]
print("\nLista z literami w małych literach:", lista_male_litery)