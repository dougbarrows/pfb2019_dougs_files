#!/usr/bin/env python3

number = 32

if number > 0:
	print("positive")
	if number < 50:
		print(" and less than 50")
		if number % 2 == 0:
			print("and it is even")
		else:
			print("and it is odd")
	if number > 50:
		if number % 3 == 0:
			print("is larger than 50 and divisible by3..!")
elif number < 0:
	print("negative")
else:
	print("its zero")
