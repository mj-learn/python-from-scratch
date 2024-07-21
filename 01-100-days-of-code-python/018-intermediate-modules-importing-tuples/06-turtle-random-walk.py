from turtle import Turtle, Screen
from random import choice

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


def random_walk():
    t = Turtle()
    t.speed(8)
    t.pensize(15)

    for _ in range(300):
        t.pencolor(choice(colors))
        t.forward(35)
        t.setheading(choice([90, 180, 270, 360]))

    screen = Screen()
    screen.exitonclick()


random_walk()
