#9. Create a function to count the number of vowels in a given string
string='omkar babar'
list1=['a','e','i','o','u']
count=0
for i in range(len(string)):
    if string[i] in list1:
        print("this is vowel",i)
        count += 1
    else:
        print("this is not a vowel",i)
print("Number of vowels in the given string is: ",count)    