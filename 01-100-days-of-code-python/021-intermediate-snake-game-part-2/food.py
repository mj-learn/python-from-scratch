from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.teleport(self._random_x_or_y(), self._random_x_or_y())

    @staticmethod
    def _random_x_or_y():
        return randint(-380, 380)

    def change_position(self):
        self.teleport(self._random_x_or_y(), self._random_x_or_y())
