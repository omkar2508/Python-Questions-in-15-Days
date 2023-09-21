#Given a list of names, print all names starting with the letter 'A'

list = ['Akash', 'Nikhil', 'anjeet', 'Abhay','all']

check = 'A'
print("The original list : " + str(list))

res = [idx for idx in list if idx[0].lower() == check.lower()]

print("The list of matching first letter : " + str(res))
 