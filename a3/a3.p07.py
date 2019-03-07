"""
JTSK-350111
problem 3.7.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

ch=input("Enter a character:")
while not 'A'<=ch<='Z':
    ch=input("Invalid character, enter a uppercase character:")
n=int(input("Enter an integer:"))
while not 0<=n<=32:
    n=int(input("Invalid integer,enter an integer between 0-32:"))
a=0
while a<=n:
    print(chr((ord(ch)+a)))
    a+=1
