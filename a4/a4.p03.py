"""
JTSK-350111
problem 4.3.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def to_liter(gallon,cup):
    return ((gallon*3.7854)+(cup*0.2366))

gallons=float(input("Enter gallons: "))
cups=float(input("Enter cups: "))

print("That converted to liters is:",to_liter(gallons,cups))
