from turtle import Turtle, Screen

guido = Turtle()

for _ in range(4):
    guido.forward(100)
    guido.left(90)

screen = Screen()
screen.exitonclick()
