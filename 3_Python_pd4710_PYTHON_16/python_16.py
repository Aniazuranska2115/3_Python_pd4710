import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

proby = ['Proba1', 'Proba2', 'Proba3']
ekspresja = np.array([
    [5.1, 2.3, 7.8],  # Ekspresja GenA
    [3.2, 4.5, 6.1],  # Ekspresja GenB
    [4.8, 5.5, 3.9]   # Ekspresja GenC
])
geny = ['GenA', 'GenB', 'GenC']

plt.figure(figsize=(8, 5))
for i, gen in enumerate(geny):
    plt.plot(proby, ekspresja[i], marker='o', label=gen)
plt.title("Zmiany ekspresji genów w próbkach")
plt.xlabel("Próbki")
plt.ylabel("Ekspresja")
plt.legend()
plt.grid()
plt.show()

x = np.arange(len(proby))
width = 0.2
plt.figure(figsize=(8, 5))
for i, gen in enumerate(geny):
    plt.bar(x + i * width, ekspresja[i], width, label=gen)
plt.xticks(x + width, proby)
plt.title("Porównanie ekspresji genów w próbkach")
plt.xlabel("Próbki")
plt.ylabel("Ekspresja")
plt.legend()
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(ekspresja[0], ekspresja[1], color='r', label='GenA vs GenB')
plt.title("Porównanie ekspresji GenA i GenB")
plt.xlabel("Ekspresja GenA")
plt.ylabel("Ekspresja GenB")
plt.legend()
plt.grid()
plt.show()

data = {
    'Gen': np.repeat(geny, len(proby)),
    'Proba': proby * len(geny),
    'Ekspresja': ekspresja.flatten()
}
df = pd.DataFrame(data)
plt.figure(figsize=(8, 5))
sns.violinplot(x='Gen', y='Ekspresja', data=df)
plt.title("Rozkład ekspresji genów (violin plot)")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Gen', y='Ekspresja', data=df)
plt.title("Rozkład ekspresji genów (box plot)")
plt.show()

plt.figure(figsize=(8, 5))
for i, gen in enumerate(geny):
    plt.plot(proby, ekspresja[i], marker='o', label=gen)
plt.title("Zmiany ekspresji genów w próbkach")
plt.xlabel("Próbki")
plt.ylabel("Ekspresja")
plt.legend()
plt.grid()
plt.savefig('ekspresja_genow.png')
print("Wykres zapisano do pliku ekspresja_genow.png.")