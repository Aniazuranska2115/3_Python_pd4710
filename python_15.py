import numpy as np
import pandas as pd

dane = {
    'Gen': ['GenA', 'GenB', 'GenC', 'GenD'],
    'Proba1': [5.1, 2.3, np.nan, 4.4],
    'Proba2': [3.2, 4.5, 3.9, np.nan],
    'Proba3': [6.3, 5.6, np.nan, 6.6]
}

df = pd.DataFrame(dane)
print("Pierwotny DataFrame:")
print(df)

print("\nBrakujące dane (NaN) w DataFrame:")
print(df.isna())

df_bez_nan = df.dropna()
print("\nDataFrame po usunięciu wierszy z brakującymi danymi:")
print(df_bez_nan)

df_uzupelniony = df.copy()
df_uzupelniony['Proba1'].fillna(df['Proba1'].mean(), inplace=True)
df_uzupelniony['Proba2'].fillna(df['Proba2'].mean(), inplace=True)
df_uzupelniony['Proba3'].fillna(df['Proba3'].mean(), inplace=True)
print("\nDataFrame po uzupełnieniu brakujących danych średnimi wartościami:")
print(df_uzupelniony)

genA_dane = df_uzupelniony[df_uzupelniony['Gen'] == 'GenA']
print("\nDane dotyczące genu GenA:")
print(genA_dane)

srednia_ekspresja = df_uzupelniony[['Proba1', 'Proba2', 'Proba3']].mean()
print("\nŚrednia ekspresja genów dla każdej z próbek:")
print(srednia_ekspresja)

geny_filtrowane = df_uzupelniony[df_uzupelniony['Proba1'] > 4]
print("\nGeny, których ekspresja w próbce 1 wynosi więcej niż 4:")
print(geny_filtrowane)

df_uzupelniony.to_csv('wynik.csv', index=False)
print("\nWynikowy DataFrame zapisano do pliku wynik.csv.")