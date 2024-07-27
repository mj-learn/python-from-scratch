from turtle import Turtle
import time

STRETCH_WIDTH = 5
STRETCH_LENGTH = 1


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)

    def go_to_right(self):
        self.goto(360, 0)

    def go_to_left(self):
        self.goto(-360, 0)

    def move_up(self):
        self.sety(self.ycor() + 15)

    def move_down(self):
        self.sety(self.ycor() - 15)
