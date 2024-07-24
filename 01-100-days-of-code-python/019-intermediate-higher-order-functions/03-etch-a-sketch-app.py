from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def go_forwards():
    return tim.forward(10)


def go_backwards():
    return tim.backward(10)


def counter_clockwise():
    return tim.left(10)


def clockwise():
    return tim.right(10)


def clear_screen():
    tim.clear()
    tim.teleport(0, 0)
    tim.setheading(0)


screen.listen()
screen.onkey(go_forwards, "w")
screen.onkey(go_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
