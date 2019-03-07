"""
JTSK-350111
problem 4.2.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def convert(miles):
    return (miles*1.609344)

miles=float(input("Enter the number of miles: "))
print("The miles converted to kilometers is: ",convert(miles))
