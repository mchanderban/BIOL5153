#!/usr/bin/env python3

dna = "ACTGTACGTGCACTGATC"

print(dna)

replacement1 = dna.replace('A', 't')
replacement2 = replacement1.replace('T', 'a')
replacement3 = replacement2.replace('C', 'g')
replacement4 = replacement3.replace('G', 'c')

dna_rc = replacement4[::-1].upper()
print(dna_rc)

G_count = dna.count('G')
C_count = dna.count('C')
G_and_C = G_count + C_count
total_length = len(dna)
gc_content = (G_count + C_count) / total_length

print("%.2f" % gc_content)

G_count2 = dna_rc.count('G')
C_count2 = dna_rc.count('C')
G_and_C2 = G_count2 + C_count2
total_length2 = len(dna_rc)
gc_content2 = (G_count2 + C_count2) / total_length2

print("%.2f" % gc_content2)
