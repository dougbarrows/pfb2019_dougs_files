#!/usr/bin/env python3


favs = {
				"book": "Jitterbug Perfume",
				"song": "Tom Petty",
				"tree": "cedar"
			}

print(favs)

print(favs['book'])

fav_thing = "tree"

print(favs[fav_thing])

print(favs['song'])

favs['organism'] = "cat"

fav_thing = "organism"

print(favs[fav_thing])


# problem 6
x = [keys for keys in favs.keys()]
str = ", "
keys_string = str.join(x)
thing = input(("which of your favorite things do you want to access - " + keys_string + "?"))

if thing not in favs:
	print("Not a valid entry!")
else:
	print(favs[thing])


# problem 7

favs['organism'] = "tetrahymena"

print(favs)


# problem 8
x = [keys for keys in favs.keys()]
str = ", "
keys_string = str.join(x)
thing = input(("which of your favorite things do you want to access - " + keys_string + "?"))

if thing not in favs:
	print("Not a valid entry!")
else:
	value_option = input(("Do you want to change your favorite " + thing + "?"))
	if value_option == "yes":
		value = input(("What is your favorite " + thing + "?"))
		favs[thing] = value

for i in favs:
	print(i, favs[i])

