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
# define gene info
	gene = (coordinates[8])
# split gene info into list based on spaces so I can grab the gene name
	gene_name = gene.split(" ")
# put organism name and gene name together for header
	header = name + " " + gene_name[1]
# print organism name, gene name, and sequence
# replace spaces with underscore in header
# add newline between header and sequence
	print(">" + header.replace(" ", "_") + "\n" +  genome[start:end])

# close GFF file
watermelon.close()
