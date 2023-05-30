from Bio import SeqIO

def filter_common_sequences(file1, file2, output_file):
    # Read sequences from the first FASTA file
    sequences1 = set()
    with open(file1, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequences1.add(str(record.seq))

    # Read sequences from the second FASTA file and filter
    common_sequences = []
    with open(file2, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequence = str(record.seq)
            if sequence not in sequences1:
                common_sequences.append(record)

    # Write the common sequences to the output file
    with open(output_file, "w") as handle:
        SeqIO.write(common_sequences, handle, "fasta")


# Usage example
file1 = "training_kunitz.fasta"  # Replace with the path to your first FASTA file
file2 = "kunitz.fasta"  # Replace with the path to your second FASTA file
output_file = "kunitz_clean.fasta"  # Replace with the desired output file path

filter_common_sequences(file1, file2, output_file)
