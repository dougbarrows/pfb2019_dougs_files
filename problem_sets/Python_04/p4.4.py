#!/usr/bin/env python3

#for i in range(101):

count = 1
while(count<101):
	print(count)
	count+=1

count = 1
while count < 1000:
	if count == 1:
		factorial = 2
		count +=1
	else:
		factorial = factorial * (count+1)
		count+=1

print(factorial)
