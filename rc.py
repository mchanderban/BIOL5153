#!/usr/bin/env python3


from Bio import SeqIO

# declare DNA sequence
dna = "ACTGTACGTGCACTGATC"

# DNA sequence could have lower case so...
dna = dna.upper()

# print upper case
print(dna)

# count each NT
# assuming all AGCT
a_count = dna.count('A')
t_count = dna.count('T')
c_count = dna.count('C')
g_count = dna.count('G')

# calculate DNA length
dna_length = len(dna)

# calculate AT fraction
at_content = (a_count + t_count) / dna_length

# print AT content to 2 decimal places
print("%.2f" % at_content)

# calculate GC fraction
gc_content = (g_count + c_count) / dna_length

# calculate GC content to 2 decimal places
print("%.2f" % gc_content)

# complements
replacement1 = dna.replace('A', 't')
replacement2 = replacement1.replace('T', 'a')
replacement3 = replacement2.replace('C', 'g')
replacement4 = replacement3.replace('G', 'c')

# reverse
dna_rc = replacement4[::-1].upper()
print(dna_rc)

# GC content of reverse complement
G_count2 = dna_rc.count('G')
C_count2 = dna_rc.count('C')
G_and_C2 = G_count2 + C_count2
total_length2 = len(dna_rc)
gc_content2 = (G_count2 + C_count2) / total_length2

print("%.2f" % gc_content2)

# file_name, file_type
for record in SeqIO.parse("seq.fasta", "fasta"):
    print(record.id)

for sequence in SeqIO.parse("seq.fasta", "fasta"):
	print(sequence.seq)
	print(sequence.seq.reverse_complement())
