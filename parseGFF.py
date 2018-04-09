#!/usr/bin/env python3

import argparse

# create an ArgumentParser object ('parser') that will hold all the info necessary to parse the command line
parser = argparse.ArgumentParser(description="This script extracts sequences from FASTA file based on coordinates")

# use the add_argument() method to add a positional argument

parser.add_argument("fasta", help="name of FASTA file")

parser.add_argument("gff", help="name of GFF file")

# parse the arguments
args = parser.parse_args()

print("We're gonna open this FASTA file:", args.fasta)

print("Open this GFF file:", args.gff)

#######################

from Bio import SeqIO
fasta = SeqIO.read(args.fasta, "fasta")

# open GFF file
gff = open(args.gff)

# read GFF file line by line using for loop
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
# print organism name, gene name, and sequence
# replace spaces with underscore in header
# add newline between header and sequence
	print(">" + header.replace(" ", "_") + "\n" +  fasta.seq[start:end])

