'''
Script to transform FASTA/MSA file to NEXUS file for BEAST analysis

WARNING: you need the biopython package to run this script

'''
from Bio import SeqIO 
import argparse

# Definition of the arguments we need to execute the script
argument_to_use = argparse.ArgumentParser()
argument_to_use.add_argument("path_of_input_file", type=str,
                             help="The path to the file we need to convert")
argument_to_use.add_argument("path_of_output_file", type=str,
                             help="The path and the name of the output NEXUS file")

# Extraction of the input arguments
args = argument_to_use.parse_args()
filename = args.path_of_input_file
output_filename = args.path_of_output_file


def get_len_of_seq():
    '''Function to get the length of the sequences'''
    input_filename = filename
    len_of_seq = int()
    with open(input_filename, 'r') as file:
        for seq_to_read in SeqIO.parse(file, "fasta"):
            len_of_seq = len(seq_to_read)
    return len_of_seq


def read_fasta() -> list[str]:
    '''Function to read the FASTA file'''
    input_filename = filename
    sequences_list = list()
    with open(input_filename, 'r') as file:
        for seq_to_read in SeqIO.parse(file, "fasta"):
            sequences_list.append(f"{seq_to_read.id} {seq_to_read.seq}" )
    return sequences_list


def transform(list_of_seq: list[str]) -> str:
    '''Function to transform the seqences into a big str'''
    len_of_file = len(list_of_seq)
    len_of_seq = get_len_of_seq()
    seqences = list_of_seq
    with open(output_filename, "w") as file:
        file.write(f"#NEXUS{"\n"}BEGIN DATA;{"\n"}{"\t"}DIMENSIONS NTAX={len_of_file} NCHAR={len_of_seq};{"\n"}{"\t"}FORMAT DATATYPE=DNA GAP=- MISSING=n;{"\n"}{"\t"}MATRIX{"\n"}")
        for sample in seqences:
            file.write(sample + "\n")
        file.write(f";{"\n"}End;")


if __name__ == "__main__":

    transform(read_fasta())


