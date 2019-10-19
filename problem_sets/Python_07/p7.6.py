#!/usr/bin/env python3

import re

with open("Python_07_ApoI.fasta", "r") as fo:
	file_read = fo.read()
	file_read_noNew = re.sub("\n", "", file_read)
	for match in re.finditer(r"([AG]AATT[CT])", file_read_noNew):
		to_sub = match.group(1)[0] + "^" + match.group(1)[1:]
		file_read_noNew  = re.sub(match.group(1), to_sub, file_read_noNew)
	print(file_read_noNew)
