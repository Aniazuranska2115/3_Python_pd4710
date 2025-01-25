import os
import pandas as pd
import matplotlib.pyplot as plt

def read_sequences(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Plik {file_path} nie istnieje.")

    sequences = []
    names = []
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith(">"):
                names.append(line.strip())
            else:
                sequences.append(line.strip())

    return names, sequences

def is_valid_sequence(sequence):
    return all(nucleotide in "ACGT" for nucleotide in sequence)

def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100 if sequence else 0

def process_sequences(names, sequences):
    data = []
    seen = set()
    for name, sequence in zip(names, sequences):
        if sequence not in seen and is_valid_sequence(sequence):
            seen.add(sequence)
            gc_content = calculate_gc_content(sequence)
            data.append({"Name": name, "Sequence": sequence, "Length": len(sequence), "GC_Content": gc_content})

    return data

def visualize_data(df):
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 3, 1)
    plt.hist(df["Length"], bins=10, color="skyblue", edgecolor="black")
    plt.title("Histogram długości sekwencji")
    plt.xlabel("Długość")
    plt.ylabel("Liczba sekwencji")

    plt.subplot(1, 3, 2)
    plt.scatter(df["Length"], df["GC_Content"], color="green", alpha=0.6)
    plt.title("GC Content vs Długość")
    plt.xlabel("Długość")
    plt.ylabel("GC Content (%)")

    plt.subplot(1, 3, 3)
    plt.boxplot(df["GC_Content"], patch_artist=True, boxprops=dict(facecolor="orange", color="black"))
    plt.title("Rozkład GC Content")
    plt.ylabel("GC Content (%)")

    plt.tight_layout()
    plt.show()

def main():
    file_path = "sekwencje.txt"

    try:
        names, sequences = read_sequences(file_path)
    except FileNotFoundError as e:
        print(e)
        return

    user_sequence = input("Podaj swoją sekwencję DNA: ").strip().upper()
    if is_valid_sequence(user_sequence):
        names.append(">User_Sequence")
        sequences.append(user_sequence)

        with open(file_path, "a") as f:
            f.write(f">User_Sequence\n{user_sequence}\n")
    else:
        print("Podana sekwencja jest niepoprawna i nie zostanie dodana.")

    data = process_sequences(names, sequences)

    df = pd.DataFrame(data)

    print("\nDataFrame:")
    print(df)

    visualize_data(df)

if __name__ == "__main__":
    main()
