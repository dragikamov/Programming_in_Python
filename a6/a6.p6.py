"""
JTSK-350111
problem 6.6.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

from turtle import Turtle
t=Turtle()
t.screen.setup(width=700, height=700)

t.pencolor('red')
t.up()
t.goto(0,-25)
t.down()
x=0
m=int(input("Enter how many stars: "))
for n in range (m):
    for i in range(5):
        t.forward(50)
        t.right(144)

    t.up()
    x+=360/m
    t.setheading(x)
    t.forward(50)
    t.down()
    t.setheading(0)


t.up()
t.home()
t.hideturtle()
