#!/usr/bin/env python3

import sys
import re

class FASTAERROR(Exception):
	pass

class WrongNTERROR(Exception):
	pass

try:
	suffixes = (".fa", ".fasta", ".nt")
	if not sys.argv[1].endswith(suffixes):
		raise FASTAERROR("file needs to end in .fa, .fasta, or .nt!")
	test = open (sys.argv[1], "r")
	test.close()
except IndexError:
	print("Please provide a file name")
	exit()
except FileNotFoundError:
	print("The file was not found, please provide a valid file")
	exit()
except FASTAERROR:
	print("file needs to end in .fa, .fasta, or .nt!")
	exit()	

with open(sys.argv[1], "r") as fo, open("Python_08.codons-6frames.nt", "w") as all_frames_file:
	
	
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
			try:
				for nt in line_st:
					if nt not in "AGCTN\n":
						raise WrongNTERROR("You can only have ACGT or N in your sequence")
			except WrongNTERROR:
				print("You can only have ACGT or N in your sequence")
				exit()	
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

with open("Python_08.codons-6frames.nt", "r") as fo, open("Python_08.codons-6frames.nt", "a") as add_to_file:
	for line in fo:
		if re.search("codons", line):	
			line = line.rstrip()
			seq_name = line + "_rev_comp"
		else:

			dna_upper = line.upper()

			dna_complement = dna_upper.replace("C", "c")
			dna_complement = dna_complement.replace("T", "t")
			dna_complement = dna_complement.replace("G", "C")
			dna_complement = dna_complement.replace("c","G")
			dna_complement = dna_complement.replace("A","T")
			dna_complement = dna_complement.replace("t", "A")

			reverse_comp = dna_complement[::-1]
		
			add_to_file.write(seq_name + reverse_comp + "\n\n")

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

with open("Python_08.codons-6frames.nt", "r") as fo, open("Python_08.translated.aa", "w") as prot_write, open("Python_08.translated-longest.aa", "w") as longest_orf_write:
	for line in fo:
		if re.search("codons", line):
			line = line.rstrip()
			seq_name = line + "_prot"
			prot_write.write(seq_name + '\n')
			longest_orf_write.write(seq_name + '\n')
		elif re.search(r"[\w]", line): # somehow inserted an empty line in between some sequences, so need ot make sure we skip those. 
			for match in re.finditer(r"([AGCT]{3})", line):
				line = (re.sub(match.group(1), translation_table[match.group(1)], line))
				line = line.replace(" ", "")
				orfs = re.findall(r"[M][A-Z]*[\*]", line)
				if len(orfs) > 0:
					orf_long = sorted(orfs, key = len, reverse = True)[0][0:-1] + '\n'
				else:
					orf_long = "no open reading frame\n"
			prot_write.write(line)
			longest_orf_write.write(orf_long)

