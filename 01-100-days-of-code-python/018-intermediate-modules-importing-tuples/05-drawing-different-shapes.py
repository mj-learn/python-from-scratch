# Instructions
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen
import random

T = Turtle()
T.speed(4)
T.pensize(3)

colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

for i in range(3, 11):
    T.pencolor(random.choice(colors))
    angle = 360 / i  # to calculate only once for a shape (code performance)
    for j in range(i):
        T.forward(140)
        T.right(angle)


screen = Screen()
screen.exitonclick()
