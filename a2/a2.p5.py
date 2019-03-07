"""
JTSK-350111
problem 2.5.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

m=int(input("Enter total number of minutes: "))
if m<0:
    print("Invalid number")
else:
    hour=m//60
    minutes=m%60
    print("Hour: ",hour," minutes: ",minutes)
