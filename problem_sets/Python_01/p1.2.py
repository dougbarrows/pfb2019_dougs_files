#!/usr/bin/env python3

import sys


print("\nSimple, just typing it all out \n")
print("My name: Doug")
print("My favorite color: blue")

fav_activity = "python"
print("My favorite activity:", fav_activity)

print("My favorite animal: cat \n")

print("done with system arguments!! \n")

print("My name: " +  sys.argv[1])
print("My favorite color: " + sys.argv[2])
print("My favorite activity: " + sys.argv[3])
print("My favorite animal: " + sys.argv[4], "\n")


print("print all in one print statement! \n")

print("My name:", sys.argv[1], "\n"+ "My favorite color:", sys.argv[2], "\n" +  "My favorite activity:", sys.argv[3], "\n" + "My favorite activity:", sys.argv[4])
