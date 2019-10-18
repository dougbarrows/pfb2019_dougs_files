#!/usr/bin/env python3


myList = [101,2,15,22,95,33,2,27,72,15,52]

for i in myList:
	if i%2 == 0:
		print(i)

myList_sorted = sorted(myList)

print(myList_sorted)

even = 0
odd = 0
for i in myList:
	if i%2 == 0:
		even += i
	else:
		odd += i

print("Sum of even numbers: {}\nSum of odds: {}".format(even, odd))
