#!/usr/bin/env python3

import argparse
from Bio import SeqIO

# define functions

# argparse
def get_args():
	# create an ArgumentParser object ('parser') that will hold all the info necessary to parse the command line
	parser = argparse.ArgumentParser(description="This script extracts sequences from FASTA file based on coordinates and calculates the reverse complement if necessary")
	# use the add_argument() method to add a positional argument
	parser.add_argument("fasta", help="name of FASTA file")
	parser.add_argument("gff", help="name of GFF file")
	# parse the arguments
	return parser.parse_args()

args = get_args()

# function to parse GFF files
def GFF():
	# read GFF file line by line using for loop
	fasta = SeqIO.read(args.fasta, "fasta")
	gff = open(args.gff)
	for line in gff:
		# split string into list based on tabs
		coordinates = line.split("\t")
		# define start and end coordinates as integers
		# subtract one from start because genome has 1-based numbering
		start = int(coordinates[3]) - 1
		end = int(coordinates[4])
		# define organism name
		name = (coordinates[0])
		# define gene info
		gene = (coordinates[8])
		# split gene info into list based on spaces so I can grab the gene name
		gene_name = gene.split(" ")
		# put organism name and gene name together for header
		header = name + " " + gene_name[1]
		# grab strand orientation
		strand = (coordinates[6])
		# print(strand)
		if strand == "+":
			print(">" + header.replace(" ", "_") + "\n" +  fasta.seq[start:end])

# reverse complement
def rev_comp():
	# read GFF file line by line using for loop
	fasta = SeqIO.read(args.fasta, "fasta")
	gff = open(args.gff)
	for line in gff:
		# split string into list based on tabs
		coordinates = line.split("\t")
		# define start and end coordinates as integers
		# subtract one from start because genome has 1-based numbering
		start = int(coordinates[3]) - 1
		end = int(coordinates[4])
		# define organism name
		name = (coordinates[0])
		# define gene info
		gene = (coordinates[8])
		# split gene info into list based on spaces so I can grab the gene name
		gene_name = gene.split(" ")
		# put organism name and gene name together for header
		header = name + " " + gene_name[1]
		# grab strand orientation
		strand = (coordinates[6])
		if strand == "-":
			print(">" + header.replace(" ", "_") + "\n" +  fasta.seq[start:end].reverse_complement())

def main():
	GFF()
	rev_comp()

main()

