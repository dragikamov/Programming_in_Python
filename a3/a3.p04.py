"""
JTSK-350111
problem 3.4.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

n=int(input("Enter the nr. of minutes to be converted:"))
for curr in range(1,n+1):
    if curr==1:
        print(curr,"minute =",curr*60,"seconds")
    else:
        print(curr,"minutes =",curr*60,"seconds")
