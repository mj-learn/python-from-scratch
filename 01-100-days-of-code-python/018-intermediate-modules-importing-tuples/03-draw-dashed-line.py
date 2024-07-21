from turtle import Turtle, Screen

guido = Turtle()

for _ in range(50):
    guido.forward(10)
    if guido.isdown():
        guido.penup()
    else:
        guido.pendown()

screen = Screen()
screen.exitonclick()
