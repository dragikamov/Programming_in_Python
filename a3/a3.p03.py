"""
JTSK-350111
problem 3.3.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

n=int(input("Enter the nr. of minutes to be converted:"))
curr=1
while curr <= n:
    if curr==1:
        print(curr,"minute =",curr*60,"seconds")
    else:
        print(curr,"minutes =",curr*60,"seconds")
    curr+=1
