import random
from turtle import Turtle, Screen


def create_turtle(x, y, color):
    t = Turtle("turtle")
    t.color(color)
    t.penup()
    t.goto(x, y)
    return t


is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
winning_color = ""

screen = Screen()
screen.setup(width=500, height=400)

user_bet = ""
while user_bet not in colors:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race?\n[red, orange, yellow, greeen, blue, purple]\nEnter a color: ",
    )

for racer in range(0, 6):
    new_turtle = create_turtle(x=-230, y=y_positions[racer], color=colors[racer])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

screen.exitonclick()
