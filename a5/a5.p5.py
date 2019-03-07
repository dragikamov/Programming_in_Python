"""
JTSK-350111
problem 5.5.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def add(lst,val):
    new_lst=[]
    for elem in lst:
        new_lst.append(elem+val)
    return new_lst

def multiply(lst,val):
    new_lst=[]
    for elem in lst:
        new_lst.append(elem*val)
    return new_lst

n=int(input("Enter the number of floats: "))
lst=[]
print("Enter the list:")
for x in range(n):
    lst.append(float(input()))
print(lst)
print(add(lst,1.5))
print(multiply(lst,5))
