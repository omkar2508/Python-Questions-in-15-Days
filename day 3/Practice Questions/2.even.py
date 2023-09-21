#2. Given a list of integers, find all the even numbers and store them in a new list
list=[12,35,1,34,65,57,78,3,67,36]
list1=[]
for i in list:
    if (i%2)==0:
        list1.append(i)
print(list1)        
        