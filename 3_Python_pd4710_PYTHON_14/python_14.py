import numpy as np

macierz_ekspresji = np.array([
    [5.0, 2.5, 7.0],
    [3.2, 4.0, 6.0],
    [8.1, 9.3, 2.5],
    [4.5, 5.7, 6.9]
])

print("Pierwotna macierz ekspresji genów:")
print(macierz_ekspresji)

macierz_ekspresji_zwiekszona = macierz_ekspresji * 1.05
print("\nMacierz po zwiększeniu ekspresji o 5%:")
print(macierz_ekspresji_zwiekszona)

srednia_dla_genow = np.mean(macierz_ekspresji_zwiekszona, axis=1)
print("\nŚrednia ekspresja dla każdego genu:")
print(srednia_dla_genow)

suma_dla_prob = np.sum(macierz_ekspresji_zwiekszona, axis=0)
print("\nSuma ekspresji genów dla każdej próby:")
print(suma_dla_prob)

macierz_ekspresji_nan = macierz_ekspresji_zwiekszona.copy()
macierz_ekspresji_nan[0, 1] = np.nan
macierz_ekspresji_nan[2, 2] = np.nan

print("\nMacierz z brakującymi danymi (NaN):")
print(macierz_ekspresji_nan)

srednia_z_nan = np.nanmean(macierz_ekspresji_nan, axis=1)
print("\nŚrednia ekspresja dla każdego genu (ignorując NaN):")
print(srednia_z_nan)