from turtle import Turtle


class State:
    def __init__(self, state, x_cor, y_cor, pencolor="black"):
        self.state = state
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.pencolor = pencolor
        self.add_state_to_map()

    def add_state_to_map(self):
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.pencolor(self.pencolor)
        t.goto(self.x_cor, self.y_cor)
        t.write(self.state, align="center", font=("Arial", 10, "normal"))
