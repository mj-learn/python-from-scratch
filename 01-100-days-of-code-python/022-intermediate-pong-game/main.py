# Turtle documentation: https://docs.python.org/3/library/turtle.html
# from turtle import Screen
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

player_1 = Paddle()
player_1.go_to_left()
screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")

player_2 = Paddle()
player_2.go_to_right()
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")

ball = Ball()
speed = 0.05

is_game_on = True
while is_game_on:
    ball.move()
    # Detect collisions with the top and down walls
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_from_wall()
        speed -= 0.005

    # Detect collisions with the players
    if ball.xcor() > 350 or ball.xcor() < -350:
        if ball.distance(player_1) < 50:
            scoreboard.increase_score_player_1()
            ball.bounce_from_player()
            speed -= 0.005
        if ball.distance(player_2) < 50:
            scoreboard.increase_score_player_2()
            ball.bounce_from_player()
            speed -= 0.005

    # Detect collisions with the left and right walls
    if ball.xcor() > 370 or ball.xcor() < -370:
        is_game_on = False
        scoreboard.game_over()

    screen.update()
    time.sleep(speed)


screen.exitonclick()
