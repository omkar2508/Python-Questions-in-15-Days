#1.Create a program that takes a year as input and checks if it is a leap year or not
year=int(input("Enter the year to check that is leap year or not : "))
if (year%4)==0:
    print(year,"is leap year")
else:
    print(year,"is not a leap year")    