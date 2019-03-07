"""
JTSK-350111
problem 6.7.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

from turtle import Turtle
t=Turtle()
t.screen.setup(width=600, height=600)

def down():
    t.down()

def forward():
    t.forward(10)

def left():
    t.left(15)

def right():
    t.right(15)

def up():
    t.up()

jumpTable={}
jumpTable['D']=down
jumpTable['F']=forward
jumpTable['L']=left
jumpTable['R']=right
jumpTable['U']=up

while True:
    string=input("Enter a string for movement: ")
    if string=="":
        break
    else:
        for n in string:
            jumpTable[n]()
