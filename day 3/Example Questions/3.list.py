#Q 3: Implement a program that finds the largest number in a list.
#1st method
'''list=[12,791,66,6,76]
if list[0]>list[1] & list[0]>list[2] & list[0]>list[3] & list[0]>list[4]:
    print(list[0],"is largest number in list ")
elif list[1]>list[0] & list[1]>list[2] & list[1]>list[3] & list[1]>list[4]:
    print(list[1],"is largest number in list ")
elif list[2]>list[0] & list[2]>list[1] & list[2]>list[3] & list[2]>list[4]:
    print(list[2],"is largest number in list ")
elif list[3]>list[0] & list[3]>list[1] & list[3]>list[2] & list[3]>list[4]:
    print(list[3],"is largest number in list ")
else:
    print(list[4],"is largest number in list ")        '''

#2nd Method 
list=[12,34,76,13,8]
print("Largest number is ",max(list))