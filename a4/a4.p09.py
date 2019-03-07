"""
JTSK-350111
problem 4.9.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

#My program starts counting from 0 for the strings

s=input("Enter a string: ")
a=int(input("Enter an integer a: "))
while a<0 or a>=len(s):
    a=int(input("Invalid number, enter another int for a: "))
b=int(input("Enter an integer b: "))
while b<0 or b>=len(s):
    b=int(input("Invalid number, enter another int for b: "))
print("The string between those constrains is:", s[a:b+1])
