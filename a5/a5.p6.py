"""
JTSK-350111
problem 5.6.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def histogram(lst):
    for elem in lst:
        while elem>0:
            print("*",end="")
            elem-=1
        print("\n",end="")

n=int(input("Enter the number of integers: "))
lst=[]
print("Enter the list:")
for x in range(n):
    lst.append(int(input()))

histogram(lst)
