#!/usr/bin/env python3

import sys

number = int(sys.argv[1])

pRint("your number is", number)
if number > 0:
	print("and it is positive")
	if number < 50:
		print("and less than 50")
		if number % 2 == 0:
			print("and it is even")
		else:
			print("and it is odd")
	if number > 50:
		if number % 3 == 0:
			print("and is larger than 50 and divisible by3..!")
elif number < 0:
	print("andit is negative")
else:
	print("and its zero")
