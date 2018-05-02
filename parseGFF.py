#!/usr/bin/env python3

import argparse
import re
import os
import sys
from Bio import SeqIO
from collections import defaultdict

# define functions

# argparse
def get_args():
	# create an ArgumentParser object ('parser') that will hold all the info necessary to parse the command line
	parser = argparse.ArgumentParser(description="This script extracts sequences from FASTA file based on coordinates and calculates the reverse complement if necessary")
	# use the add_argument() method to add a required/positional argument
	parser.add_argument("fasta", help="name of FASTA file")
	parser.add_argument("gff", help="name of GFF file")
	# parse the arguments
	return parser.parse_args()

args = get_args()

# function to parse FASTA files
def parse_FASTA():
	genome = SeqIO.read(args.fasta, "fasta")
	return genome.seq

# reverse complement
def reverse_complement(genome):
	return genome.reverse_complement()

# function to parse GFF files
def parse_GFF(genome):
	# read GFF file line by line using for loop
	gff_file = open(args.gff, 'r')
	for line in gff_file:
		# split string into list based on tabs
		(seqid, source, feature, start, end, length, strand, phase, attributes) = line.split("\t")
		# define start and end coordinates as integers
		# subtract one from start because genome has 1-based numbering
		if(feature == 'CDS' or feature == 'tRNA' or feature == 'rRNA'):
			# define gene info
			# split attributes field
			atts = attributes.split(" ; ")
			# grab gene name and exon number (if present)
			gene = re.search("^Gene\s+(\S+)", atts[0])
			exon = re.search("exon\s+(\d+)", atts[0])
			fragment = genome[int(start)-1:int(end)]
			if(gene and exon):
				gene_name = ">" + seqid.replace(" ", "_") + "_" + gene.group(1) + "_" + exon.group(1)
				# make list of headers attached to exon number
				exon_list = []
				exon_list.append(gene_name)
				genes = defaultdict(dict)
				genes[start] = gene_name
				for gene, sequence in genes.items():
					print(gene_name)
			else:
				print(">" + seqid.replace(" ", "_") + "_" + gene.group(1))
			if(strand == "+"):
				print(fragment)
			else:
				print(reverse_complement(fragment))
	gff_file.close()

def main():
	genome = parse_FASTA()
	parse_GFF(genome)

main()

