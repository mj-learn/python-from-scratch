from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwerds():
    tim.forward(10)


screen.listen()
screen.onkey(fun=move_forwerds, key="space")

screen.exitonclick()
