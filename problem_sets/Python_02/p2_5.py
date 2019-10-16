#!/usr/bin/env python3


truth_var = 20
list_var = [25,30] 

if truth_var == 25: #must use '==' if it is one number, must be an iterable object (like a list) to use 'in' as below
	print(truth_var, "is 25, sweet!!")
elif truth_var in list_var :
	print(truth_var, "is in the list, sweet!")
elif truth_var < 25:
	print(truth_var, "is less than 25, okay...")
elif truth_var > 25:
	print(truth_var, "is greater than 25, not bad")
else:
	print(truth_var, "how did this happen?")

