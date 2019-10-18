#!/usr/bin/env python3

import re

with open('Python_07_nobody.txt', 'r') as fo:
	file = fo.read()
	print(file)

	for match in  re.finditer(r"Nobody", file):
		start = match.start(0)
		print(start)
	

with open('Python_07_nobody.txt', 'r') as fo, open('Python_07_nobody_sub.txt', 'w') as nobody_sub:
	file = fo.read()
	file_sub = file.replace("Nobody", "Doug")
	nobody_sub.write(file_sub) 
