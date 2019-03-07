# Problem 9

from turtle import Turtle

t=Turtle()
t.screen.setup(width=683, height=576)
t.speed("fastest")

t.up()
t.goto(-50,0)
t.setheading(270)
t.color('red')
t.down()
t.circle(100)

t.up()
t.goto(50,0)
t.setheading(90)
t.color('green')
t.down()
t.begin_fill()
t.circle(100)
t.end_fill()

t.hideturtle()

t.screen.exitonclick()