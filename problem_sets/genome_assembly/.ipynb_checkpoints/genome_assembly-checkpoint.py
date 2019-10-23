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
        
print("L50:", len(records[15]))
print("N50:", count)
        
        


