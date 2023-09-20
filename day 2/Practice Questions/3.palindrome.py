#3. Implement a program that checks if a given string is a palindrome
string=str(input("Enter any Palindrome Word"))
rev_string=reversed(string)
if list(string)==list(rev_string):  
    print("This is palindrome")
else:
    print("this is not palindrome")    