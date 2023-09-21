# Write a Python program to check if a given number is a prime number
num=int(input("Enter any number to check is it a prime number : "))
if num<1:
    print(num,"is not a prime number") 
elif num>1:
    for i in range(2,num):
        if (num%i)==0 :
            print(num,"is not a prime number")
        else:
            print(num,"is a prime number")
        break    

else:
    print(num,"is not a prime number like 0")            
