#!/usr/bin/env python3


import re

with open('Python_07.fasta', 'r') as fo:
	for line in fo:
		if re.search(">", line):
			#print(line)
			gene_name = re.search(r">(\S+)\s(.+)", line)
			print("id:",gene_name.group(1), "desc:",gene_name.group(2))



