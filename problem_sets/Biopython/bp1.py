#!/usr/bin/env python3



import Bio.Seq

from Bio import SeqIO

count = 0
nts = 0
GC_content = 0
for seq_record in SeqIO.parse("Python_08.fasta", "fasta"):
	if count == 0:
		short_len = len(seq_record.seq)
		long_len = len(seq_record.seq)
	else:
		if len(seq_record.seq) < short_len:
			short_len = len(seq_record.seq)
		if len(seq_record.seq) > long_len:
			long_len = len(seq_record.seq)
	GC_record = (seq_record.seq.count("G") + seq_record.seq.count("C"))/len(seq_record.seq)
	GC_content+=GC_record
	#print("ID", seq_record.id, "Desc:", seq_record.description, "\nSequence:", seq_record.seq)
	count +=1
	nts+=len(seq_record.seq)
		
GC_content_avg = GC_content/count
avg_len = nts/count

print("sequence count:", count, "\navg len:", avg_len, "\nshortest len:", short_len, "\nlongest len:", long_len, "\navg GC:", GC_content_avg)
