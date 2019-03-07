"""
JTSK-350111
problem 4.7.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

sentence=input("Enter the string: ")
n=len(sentence)
k=0
for k in range(n):
    j=k
    while j>0:
        print(" ",end="")
        j-=1
    print(sentence[k])
