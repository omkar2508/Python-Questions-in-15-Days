# Create a program that generates the Fibonacci sequence up to a given number of terms
num =int(input("enter the number: "))
num1=0
num2=1
next_num=num2
count=1
print(1,end=" ")
while count<=num:
        print(next_num,end=" ")
        count+=1
        num1=num2
        num2=next_num
        next_num=num1+num2
print()        