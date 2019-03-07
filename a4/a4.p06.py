"""
JTSK-350111
problem 4.6.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

import random
random.seed()
minval=1
maxval=50
r=random.randint(minval,maxval)
while True:
    guess=int(input("Enter your guess : "))
    if r==guess:
        print("You got it!")
        break
    elif guess<r:
        print("Your guess is too small !")
    else:
        print("Your guess is too high !")
print("Bye")
