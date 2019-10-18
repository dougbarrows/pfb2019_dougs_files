#!/usr/bin/env python3


import sys

for i in range(int(sys.argv[1]), int(sys.argv[2])):
	print( i)
	if i%2 != 0:
		print("odd:", i)
