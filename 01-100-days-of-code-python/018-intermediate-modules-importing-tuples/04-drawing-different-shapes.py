# Instructions
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen

# My solution before understand what exactly teacher wanna from me

guido = Turtle()
guido.speed(1)

for i in range(7):
    guido.circle(70 + i * 30, steps=(i + 3))


screen = Screen()
screen.exitonclick()
