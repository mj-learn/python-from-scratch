from turtle import Turtle

FONT = ("Courier", 60, "bold")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 210)
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_player_1}   {self.score_player_2}", align=ALIGN, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increase_score_player_1(self):
        self.score_player_1 += 1
        self.update_scoreboard()

    def increase_score_player_2(self):
        self.score_player_2 += 1
        self.update_scoreboard()
