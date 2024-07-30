# Turtle documentation: https://docs.python.org/3/library/turtle.html

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Snake Game Improved")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(scoreboard.game_over, "q")

while scoreboard.is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.change_position()
        snake.add_segment()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        snake.reset_snake()
        scoreboard.reset_score()

    # Detect collision with body
    if snake.detect_collision():
        snake.reset_snake()
        scoreboard.reset_score()


screen.exitonclick()
