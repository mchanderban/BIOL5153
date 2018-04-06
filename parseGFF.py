#!/usr/bin/env python3

from Bio import SeqIO

# read and store genome
genome = open("watermelon.fsa").read()

# open GFF file

# read it in line by line

	# split string on tab into list 
# use start and end coordinates to extract from genome


# open GFF file
watermelon = open("watermelon.gff")

import sys
for line in watermelon:
# split string into list based on tabs
	coordinates = line.split("\t")
	start = int(coordinates[3])
	end = int(coordinates[4])
	name = (coordinates[0])
	gene = (coordinates[8])
	print(">" + name + gene + genome[start:end])

# close GFF file
watermelon.close()
