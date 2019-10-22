#!/usr/bin/env python3

'''
with open('ss_rand5-200_v_qfo_BL50.txt', 'r') as fo, open('rand200.txt', 'w') as output_file:
	line_list = []
	line_list_temp= []
	top_line = []
	for line in fo:
		if not line.startswith('#'):
			line_list_temp  = line.split()
			if not line_list:
				line_list = line_list_temp
				if line_list_temp[2] >=  line_list[2]:
					top_line = line_list
'''
import os
import re

files = os.listdir()
good_files = []

for i in files:
	if  re.search(r"ss_rand5", i):
		good_files.append(i)


lines_dict = {}
for files in good_files: 
	with open(files, 'r') as fo:
		for line in fo:
			if not line.startswith('#'):
				lines_dict[files]  = [line.split()[2], line.split()[3], line.split()[10]]
				break

hits_data = []
fields = ["percid", "alen", "evalue", "file"]
for key, value in lines_dict.items():
		lines_dict[key].append(key)
		hits_data.append(dict(zip(fields,lines_dict[key])))


for hits in hits_data:
	print('\t'.join([hits[x] for x in ('file', 'percid', 'alen', 'evalue')]))
	

#print(lines_dict)

#print(\'t'.join(lines_dict[x] for x in ()

	
