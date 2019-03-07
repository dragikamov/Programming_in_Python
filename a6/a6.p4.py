"""
JTSK-350111
problem 6.4.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

from turtle import Turtle
t=Turtle()
t.screen.setup(width=600, height=600)

t.up()
t.pencolor('red')
t.goto(-100,0)
t.color('red')

#12tangle
t.down()
t.begin_fill()
for n in range(13):
    t.forward(53)
    t.end_fill()
    
    t.forward(94)
    
    t.begin_fill()
    t.forward(53)
    t.left(150)

#circle
t.end_fill()
t.up()
t.home()
t.down()
t.begin_fill()
t.circle(27)
t.end_fill()


#inner triangles
t.goto(-47,0)
t.left(60)
t.color('red')
t.begin_fill()

for n in range(12):
    t.begin_fill()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(120)
    t.end_fill()

#smaller triangles
t.home()
t.backward(27)
t.begin_fill()
t.left(90)
t.forward(12.5)
t.right(120)
t.forward(7)
t.right(30)
t.forward(10)
t.right(120)
t.forward(11)
t.end_fill()

for n in range(11):
    t.right(90)
    t.forward(12.5)
    t.begin_fill()
    t.forward(10)
    t.left(30)
    t.forward(7)
    t.left(120)
    t.forward(12.5)
    t.left(90)
    t.forward(11)
    t.end_fill()
    t.left(180)
    t.forward(11)

t.up()
t.home()
t.goto(-100,0)
