#!/usr/bin/env python3

count = 0
char=0
with open('Python_06.fastq') as fo:
	for line in fo:
		line = line.rstrip()
		count+=1
		char+=len(line)
	print("Number of lines:", count)
	print("Number of characters:", char)
	print("Average line length:", char/count)
