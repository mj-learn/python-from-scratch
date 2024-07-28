from turtle import Turtle

FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.teleport(-170, 260)
        self.level = 0
        self._update_scoreboard()

    def _update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="right", font=FONT)

    def increase_level(self):
        self.level += 1
        self._update_scoreboard()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)
