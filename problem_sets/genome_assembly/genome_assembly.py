#!/usr/bin/env python3

from Bio import SeqIO

records = list(SeqIO.parse("./ecoli_0.25.contigs.fasta", "fasta"))
records.sort(key=lambda r: -len(r))

length = 0
for record in records:
    length = length + len(record)

half_length = length/2
    
count = 0
length2 = 0

for record in records:
    length2 = length2 + len(record)
    if length2 < half_length:
        count +=1

# count = 16, but this is the contig before we pass the half length, so wthe next one, or count +1, is the N50 
print("L50:", len(records[16]))
print("N50:", count + 1) 
        
        


