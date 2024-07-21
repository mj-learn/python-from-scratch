import turtle as t
import random


def randon_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Using random_rgb in turtle
t.colormode(255)


def draw_spirograph(size_of_gap):
    tim = t.Turtle()
    tim.speed("fastest")
    tim.pensize(2)

    for i in range(360 // size_of_gap):
        tim.pencolor(randon_rgb())
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)
    screen = t.Screen()
    screen.exitonclick()


draw_spirograph(3)
