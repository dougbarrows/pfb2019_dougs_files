#!/usr/bin/env python3


import subprocess

names = ['BL50', 'BP62', 'VT10', 'VT160', 'VT20', 'VT40', 'VT80']

for i in range(len(names)):
	url = 'https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-200_v_qfo_' + names[i] + '.txt'
	subprocess.run(['wget', url])

for i in range(len(names)):
  url = 'https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-800_v_qfo_' + names[i] + '.txt'
  subprocess.run(['wget', url])
