#!/usr/bin/env python3

number = -2

if number > 0:
	print("positive")
	if number < 50:
		print(" and less than 50")
		if (number % 2 == 0):
			print("and it is even")
		else:
			print("and it is odd")
elif number < 0:
	print("negative")
else:
	print("its zero")
