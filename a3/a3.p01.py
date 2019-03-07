"""
JTSK-350111
problem 3.1.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

character=input("Enter a character: ")
character=ord(character)
if character<97 or character>122:
    print("The character is not lowercase.")
else:
    print("The character is lowercase.")
