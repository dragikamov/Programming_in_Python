"""
JTSK-350111
problem 6.3.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

from turtle import Turtle
t=Turtle()
t.screen.setup(width=700,height=700)

def square(n):
    for x in range(4):
        t.forward(n)
        t.left(90)

def drawBigSquare(n):
    t.up()
    t.pencolor('black')
    t.goto(n/2,n/2)
    t.setheading(180)
    t.down()
    square(n)

def drawCircles(n,r):
    t.up()
    t.pencolor('orange')
    t.goto(n/2-r,n/2)
    t.setheading(180)
    t.down()
    t.circle(r)

    t.up()
    t.goto(-n/2,n/2-r)
    t.setheading(270)
    t.down()
    t.circle(r)

    t.up()
    t.goto(-n/2+r,-n/2)
    t.setheading(0)
    t.down()
    t.circle(r)

    t.up()
    t.goto(n/2,-n/2+r)
    t.setheading(90)
    t.down()
    t.circle(r)

n=int(input("Enter size for the size of the big square: "))

drawBigSquare(n)

m=int(input("Enter size for the radius of the small circles: "))

drawCircles(n,m)
