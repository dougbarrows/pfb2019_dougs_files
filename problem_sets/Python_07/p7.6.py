#!/usr/bin/env python3

import re

seq_apo_dict = {}
keys = []
values = []
seq = ""
with open("Python_07_ApoI.fasta", "r") as fo:
 	
	for line in fo:
		if ">" in line:
			print(line)
			geneid = re.search(r">(\S+)", line)
			keys.append(geneid.group(1))

		else:

			#file_read = fo.read()
			seq = seq + line

	seq_noNew = re.sub(r"\n", "", seq)
			

	for match in re.finditer(r"([AG]AATT[CT])", seq_noNew):
		to_sub = match.group(1)[0] + "^" + match.group(1)[1:]
		seq_noNew  = re.sub(match.group(1), to_sub, seq_noNew)
	print(seq_noNew)
	values = seq_noNew.split("^")
	
	values.sort(key = len)
	
	len_dict = {}
	for value in values:
		len_dict[value] = len(value)

	print(len_dict)
	#print(values)
	#print("keys:",keys)
	#print("values:", values)
	#print("values:", values)

#seq_cut = file_read_noNew.split("^")

#print(seq_cut)
