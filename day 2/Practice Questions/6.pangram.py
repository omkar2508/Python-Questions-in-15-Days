#6. Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)
# function to check if all elements are present or not

string ="The quick brown fox jumps over the lazy dog"
string=string.replace(" ","")
string=string.lower()
alphabets="abcdefghijklmnopqrstuvwxyz"
c=0
for i in alphabets:
	if i in string:
		c+=1
if(c==len(alphabets)):
	print("The string is a pangram")
else:
	print("The string isn't a pangram")
