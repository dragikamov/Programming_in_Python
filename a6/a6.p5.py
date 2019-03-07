"""
JTSK-350111
problem 6.5.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

from turtle import Turtle
t=Turtle()
t.screen.setup(width=700, height=700)

t.pencolor('blue')
t.up()
t.goto(35,-160)
t.down()
x=0

for n in range (16):
    t.circle(40)
    t.up()
    x+=22.5
    t.setheading(x)
    t.forward(70)
    t.down()

t.up()
t.setheading(270)
t.goto(-140,0)
t.down()
t.circle(140)

t.up()
t.home()
