from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.is_game_on = True
        self.hideturtle()
        self.penup()
        self.goto(0, 365)
        self.color("white")
        self._update_high_score()
        self._update_score()

    def _update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        self.write_high_score()
        self._update_high_score()
        self.score = 0
        self._update_score()

    def increase_score(self):
        self.score += 1
        self._update_score()

    def write_high_score(self):
        if self.score > self.read_high_score():
            with open("highscore.txt", "w") as file:
                file.write(f"{self.score}")

    @staticmethod
    def read_high_score():
        with open("highscore.txt", "r") as file:
            return int(file.read())

    def _update_high_score(self):
        self.high_score = self.read_high_score()

    def game_over(self):
        self.reset_score()
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.is_game_on = False
