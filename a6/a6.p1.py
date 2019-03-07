"""
JTSK-350111
problem 6.1.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

from turtle import Turtle

n=int(input("Enter size for the size of the square: "))

t=Turtle()
t.screen.setup(width=600,height=600)

t.up()
t.forward(n/2)
t.left(90)

t.down()
t.forward(n/2)
t.left(90)

for x in range(3):
    t.forward(n)
    t.left(90)

t.forward(n/2)
t.hideturtle()
