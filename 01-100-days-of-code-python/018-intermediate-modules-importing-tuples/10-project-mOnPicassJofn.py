# Project mOnPicassJofn
# Create a copy of Damien Hirst's Cupric Nitrate painting with turtle
# Damien Hirst (Cupric Nitrate): https://www.phillips.com/detail/damien-hirst/UK010124/28
# Turtle documentation: https://docs.python.org/3/library/turtle.html

import turtle
from turtle import Turtle, Screen
import random

PALETTE = [
    (207, 160, 83),
    (55, 89, 131),
    (144, 91, 41),
    (138, 27, 49),
    (222, 206, 108),
    (132, 176, 202),
    (156, 47, 83),
    (46, 55, 103),
    (168, 159, 41),
    (129, 188, 143),
    (83, 20, 44),
    (36, 43, 69),
    (186, 94, 106),
    (185, 140, 172),
    (84, 123, 180),
    (59, 39, 31),
]

turtle.colormode(255)

mOnPicassJofn = Turtle()
mOnPicassJofn.speed("fastest")
mOnPicassJofn.hideturtle()
mOnPicassJofn.penup()
mOnPicassJofn.teleport(-250, -250)

for dot in range(1, 51):
    mOnPicassJofn.dot(20, random.choice(PALETTE))
    if dot % 10 != 0:
        mOnPicassJofn.forward(50)
    else:
        mOnPicassJofn.left(90)
        mOnPicassJofn.forward(50)
        mOnPicassJofn.left(90)
        for x in range(9):
            mOnPicassJofn.dot(20, random.choice(PALETTE))
            mOnPicassJofn.forward(50)
        mOnPicassJofn.dot(20, random.choice(PALETTE))
        if dot < 41:
            mOnPicassJofn.right(90)
            mOnPicassJofn.forward(50)
            mOnPicassJofn.right(90)


screen = Screen()
screen.exitonclick()
