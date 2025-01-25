class InvalidDNASequenceError(Exception):
    pass


def read_dna_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print(f"Zawartość pliku {filename}:\n{data}")
            return data
    except FileNotFoundError:
        print(f"Błąd: Plik {filename} nie istnieje.")
        return None


def validate_dna_sequence(sequence):
    valid_characters = {'A', 'T', 'C', 'G'}
    if not all(char in valid_characters for char in sequence):
        raise InvalidDNASequenceError(
            "Sekwencja DNA może zawierać jedynie litery A, T, C, G."
        )


def write_dna_file(filename, sequence):
    with open(filename, 'w') as file:
        file.write(sequence)
        print(f"Sekwencja została zapisana do pliku {filename}.")


def main():
    input_filename = "sekwencje.txt"
    read_dna_file(input_filename)

    try:
        user_sequence = input("Podaj nową sekwencję DNA (litery A, T, C, G): ").strip().upper()
        validate_dna_sequence(user_sequence)
    except InvalidDNASequenceError as e:
        print(f"Błąd: {e}")
        return

    output_filename = "nowa_sekwencja.txt"
    write_dna_file(output_filename, user_sequence)


if __name__ == "__main__":
    main()
