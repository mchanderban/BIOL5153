#! /usr/bin/env python3

# load required modules
from Bio import SeqIO
import argparse

# create an ArgumentParser object ('parser') that will hold all the info necessary to parse the command line
parser = argparse.ArgumentParser(description="This script filters out user-specified sequences from a FASTA file")

# use the add_argument() method to add a positional argument 
# positional arguments are required inputs, so their order/position matters
# argparse treats all options as strings unless told to do otherwise
parser.add_argument("fasta", help="name of FASTA file")

parser.add_argument("remove", help="name of file containing sequences to be removed")

# parse the arguments
args = parser.parse_args()

print("We're gonna open this FASTA file:", args.fasta)

print("filter out sequences contained in this file", args.remove)

fasta = SeqIO.parse(args.fasta, "fasta")

remove = SeqIO.read(args.remove, "fasta")

for sequence in fasta:
	if sequence.description != remove.description:
		print(sequence.format("fasta"))