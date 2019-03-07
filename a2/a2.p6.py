"""
JTSK-350111
problem 2.6.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

#The following will print the string that many times
string=str(input("Enter the string: "))
integer=int(input("Enter the integer: "))
print(string*integer)

"""
The following makes an error because it cannot multiply a string and a float

string2=str(input("Enter the string: "))
float2=float(input("Enter the float value: "))
print(string2*float2)
"""

#The following will just concatenate the strings
integer2=input("Enter the first integer: ")
integer3=input("Enter the second integer: ")
print(integer2+integer3)
