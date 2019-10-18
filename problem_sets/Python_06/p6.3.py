#!/usr/bin/env python3

seqs = {}
compl = {}
with open("Python_06.seq.txt", "r") as fo:
	for line in fo:
		geneid, seq = line.split("\t")
		seqs[geneid] = seq
		dna_upper = seq.upper()
		dna_complement = dna_upper.replace("C", "c")
		dna_complement = dna_complement.replace("T", "t")
		dna_complement = dna_complement.replace("G", "C")
		dna_complement = dna_complement.replace("c","G")
		dna_complement = dna_complement.replace("A","T")
		dna_complement = dna_complement.replace("t", "A")

		reverse_comp = dna_complement[::-1]
		compl[geneid] = reverse_comp
		print(geneid, "| reverse_complement", reverse_comp)




