#!/usr/bin/env python3

import sys
import re



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
			 



		



