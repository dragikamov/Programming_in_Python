"""
JTSK-350111
problem 3.6.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

ch=input("Enter a character:")
n=int(input("Enter an integer:"))
a=0
while a<=n:
    print(chr((ord(ch)+a)))
    a+=1
