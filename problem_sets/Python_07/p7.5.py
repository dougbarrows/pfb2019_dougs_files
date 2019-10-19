#!/usr/bin/env python3

import re


fastaDict = {}
header_count = 0
headers = []
seqs = []
seq_count = 0
with open("../Python_06/Python_06_RC.txt", "r") as fo:
	for line in fo:
		if ">" in line:
			geneid_re = re.search(r">\s(\S+)", line)
			geneid = geneid_re.group(1)
			headers.append(geneid)
		else:
			seq_re = re.search(r"[A-Z\n]+", line)
			seq = seq_re.string
			seq_nonewLine = re.sub("\n", "", seq) 	
			seqs.append(seq_nonewLine) 
	
	count2 = 0
	for i in headers:
		fastaDict[headers[count2]] = seqs[count2]
		count2+=1

print(fastaDict)
			 
