from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.teleport(0, -270)

    def go_to_bottom(self):
        self.sety(-300)

    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_left(self):
        self.setx(self.xcor() - 20)

    def move_right(self):
        self.setx(self.xcor() + 20)
