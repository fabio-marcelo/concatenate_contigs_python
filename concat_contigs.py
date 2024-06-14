from Bio import SeqIO
import sys
import os

# Input and output file paths
input_fasta = sys.argv[1]
output_fasta = sys.argv[2]

# Extract the base filename without extension
input_filename = os.path.splitext(os.path.basename(input_fasta))[0]

# Initialize an empty string to hold the concatenated sequence
concatenated_sequence = ""

# Read the multi-FASTA file
with open(input_fasta, 'r') as infile:
    for record in SeqIO.parse(infile, 'fasta'):
        # Concatenate each sequence to the concatenated_sequence string
        concatenated_sequence += str(record.seq)

# Write the concatenated sequence to a new FASTA file
with open(output_fasta, 'w') as outfile:
    # Write the single concatenated contig to the output file
    outfile.write(f">{input_filename}\n")
    # Optionally, you can format the sequence into lines of fixed length (e.g., 80 characters per line)
    for i in range(0, len(concatenated_sequence), 80):
        outfile.write(concatenated_sequence[i:i+80] + '\n')

print(f"Concatenated sequence written to '{output_fasta}' successfully.")
