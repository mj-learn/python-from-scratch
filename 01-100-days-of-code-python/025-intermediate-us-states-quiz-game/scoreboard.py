from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.teleport(-110, 210)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}/50", align="center", font=("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
