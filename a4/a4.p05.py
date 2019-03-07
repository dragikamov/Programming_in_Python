"""
JTSK-350111
problem 4.5.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

from math import pi
def volume(r):
    return (4*pi*(r**3)/3)

r=float(input("Enter the radius: "))
print("The volume of the sphere is:",volume(r))
