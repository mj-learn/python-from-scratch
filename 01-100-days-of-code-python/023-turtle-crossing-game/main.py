from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from traffic import Traffic
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
traffic = Traffic()


screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 30 and abs(a.ycor() - b.ycor()) < 20


is_game_on = True
while is_game_on:
    # Detect collision with top wall
    if player.ycor() > 300:
        scoreboard.increase_level()
        traffic.increase_speed()
        player.go_to_bottom()

    # Detect collision with left or right walls and cars
    if player.xcor() > 280 or player.xcor() < -280 or traffic.is_collided_with(player):
        is_game_on = False
        scoreboard.game_over()

    traffic.create_car()
    traffic.move_cars()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
