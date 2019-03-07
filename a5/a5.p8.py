"""
JTSK-350111
problem 5.8.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def overlapping(list1,list2):
    for elem1 in list1:
        for elem2 in list2:
            if elem1==elem2:
                return True

lst1=[]
lst2=[]
print("Enter the first list:")
while True:
    y=int(input())
    if y<0:
        break
    else:
        lst1.append(y)
print("Enter the second list:")
while True:
    y=int(input())
    if y<0:
        break
    else:
        lst2.append(y)

if(overlapping(lst1,lst2)==True):
    print("The two lists are overlapping.")
else:
    print("The two lists are not overlapping.")
