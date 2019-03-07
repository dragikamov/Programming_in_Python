"""
JTSK-350111
problem 2.4.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

celsius=float(input("Enter the degrees in celsius: "))
fahrenheit=(9*celsius/5)+32
if fahrenheit<=32:
    print("Cold")
elif fahrenheit>=104:
    print("Hot")

