#4. Create a function to reverse a given string'
#first method
'''string=str(input("Enter a string: "))
revese_string=reversed(string)
list1=list(revese_string)
sum=list1[0]+list1[1]+list1[2]+list1[3]+list1[4]
print("Reversed String :",sum)'''

#second method
s = "Python bhai"
def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str


print("The original string is : ",s)

print("The reversed string is : ",reverse(s))
