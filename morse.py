#morse
morse = {"A": ".-", "B": "-...", "C" : "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-.."}

#input
mode = int(input("Type 0 to convert to morse\nType 1 to convert from morse\nType 0 or 1: "))
input = input("\nEnter message: ").upper().split(" ")

#from morse
if mode == 0:
	for i in input:
		for x in i :
			print(" " + morse[x], end = "")

#to morse
if mode == 1:	
	for i in input:
		for x in list(morse.keys()):
		    if morse[x] == i:
		        print(x, end = "")