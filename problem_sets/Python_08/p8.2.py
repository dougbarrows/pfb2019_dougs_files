#!/usr/bin/env python3

import sys
import re

with open (sys.argv[1], "r") as fo, open("Python_08.codons-all-frames_final.nt", "w") as all_frames_file:
	
	genes = ""
	seq = ""
	my_dict = {}
	for line in fo:
		if ">" in line:
			seq = ""
			genes_re = re.search(r">(\S+)", line)
			gene = genes_re.group(1)
		else:
			line_st = line.rstrip()
			seq = seq + line_st
			my_dict[gene] = seq
	
	

	for key,value in my_dict.items():
		frame1_codons = []
		frame2_codons = []
		frame3_codons = []
		output1 = ""
		output2 = ""
		output3 = ""
		#### frame 1
		count_three = 0
		while count_three < len(value):
			frame1_codons.append(value[count_three:count_three+3])
			count_three+=3
		if len(frame1_codons[len(frame1_codons) - 1]) != 3:
			frame1_codons.pop()
		frame1_codons.append('\n')
		temp1 = key + "_frame1_codons"
		output1 = temp1 + "\n" + " ".join(frame1_codons)
		all_frames_file.write(output1)	
		
		#### frame 2
		value2 = value[1:]
		count_three = 0
		while count_three < len(value2):
			frame2_codons.append(value2[count_three:count_three+3])
			count_three+=3
		if len(frame2_codons[len(frame2_codons) - 1]) != 3:
			frame2_codons.pop()
		frame2_codons.append('\n')
		temp2 = key + "_frame2_codons"
		output2 = temp2 + "\n" + " ".join(frame2_codons)
		all_frames_file.write(output2)

	### frame 3	
		value3 = value[2:]
		count_three = 0
		while count_three < len(value3):
			frame3_codons.append(value3[count_three:count_three+3])
			count_three+=3
		if len(frame3_codons[len(frame3_codons) - 1]) != 3:
			frame3_codons.pop()
		frame3_codons.append('\n')
		temp3 = key + "_frame3_codons"
		output3 =  temp3 + "\n" + " ".join(frame3_codons)
		all_frames_file.write(output3)
	

with open("Python_08.codons-all-frames_final.nt", "r") as fo, open("Python_08.codons-6frames.nt", "w") as rev_comp:
	rev_comp_list = []
	seq_name_list = []
	for line in fo:
		if re.search("codons", line):
			seq_name = line
		else:

			dna_upper = line.upper()

			dna_complement = dna_upper.replace("C", "c")
			dna_complement = dna_complement.replace("T", "t")
			dna_complement = dna_complement.replace("G", "C")
			dna_complement = dna_complement.replace("c","G")
			dna_complement = dna_complement.replace("A","T")
			dna_complement = dna_complement.replace("t", "A")

			reverse_comp = dna_complement[::-1]
			
			rev_comp_list.append(reverse_comp)
		
			rev_comp.write(seq_name + reverse_comp + "\n\n")
