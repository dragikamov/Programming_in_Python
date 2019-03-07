"""
JTSK-350111
problem 5.7.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

lst=[]
print("Enter the integers: ")
while True:
    n=int(input())
    if n==0:
        break
    else:
        lst.append(n)

lst.sort()
print("The minimum value is:",lst[0])
print("The maximum value is:",lst[len(lst)-1])
