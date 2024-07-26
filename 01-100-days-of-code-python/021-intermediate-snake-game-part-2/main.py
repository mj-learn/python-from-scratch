# Turtle documentation: https://docs.python.org/3/library/turtle.html

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.change_position()
        snake.add_segment()
        scoreboard.increase_score()

    # Detect collision with food
    if snake.head.xcor() > 400 or snake.head.xcor() < -400 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with body
    if snake.detect_collision():
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
