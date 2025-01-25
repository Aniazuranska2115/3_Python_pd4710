from Bio import Entrez, SeqIO
from Bio.Align import PairwiseAligner

Entrez.email = "your_email@example.com"
ids = ["JX669568", "JX669571"]
sequences = []

for genbank_id in ids:
    with Entrez.efetch(db="nucleotide", id=genbank_id, rettype="fasta", retmode="text") as handle:
        seq_record = SeqIO.read(handle, "fasta")
        sequences.append(seq_record)

with open("sekwencje.fasta", "w") as fasta_file:
    SeqIO.write(sequences, fasta_file, "fasta")

print("Sekwencje zapisano do pliku sekwencje.fasta.")

sequences = list(SeqIO.parse("sekwencje.fasta", "fasta"))
seq1 = str(sequences[0].seq)
seq2 = str(sequences[1].seq)

aligner = PairwiseAligner()
aligner.mode = "global"
alignments = aligner.align(seq1, seq2)

best_alignment = alignments[0]
print("Najlepsze dopasowanie:")
print(best_alignment)
print(f"Punktacja dopasowania: {best_alignment.score}")
