#!/usr/bin/env python3

from Bio import SeqIO

# read and store genome
genome = open("watermelon.fsa").read()

# open GFF file
watermelon = open("watermelon.gff")

# read GFF file line by line using for loop
for line in watermelon:
# split string into list based on tabs
	coordinates = line.split("\t")
# define start and end coordinates as integers
# add 194 to each (length of header in genome file)
	start = int(coordinates[3]) + 194
# add 1 to end so it includes last nucleotide
	end = int(coordinates[4]) + 195
# define organism name
	name = (coordinates[0])
# define gene name
	gene = (coordinates[8])
# print organism name, gene name, and sequence
	print(">" + name + " " + gene + genome[start:end])

# close GFF file
watermelon.close()
