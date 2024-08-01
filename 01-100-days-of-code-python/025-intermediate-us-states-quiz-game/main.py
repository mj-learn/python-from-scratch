import pandas
from turtle import Screen
from scoreboard import Scoreboard
from states import State

data = pandas.read_csv("50_states.csv")
guessed_states = []


screen = Screen()
screen.title("U.S. States Quiz Game")
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")
screen.tracer(0)

scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    guessed_states_len = len(guessed_states)
    answer_state = screen.textinput(f"{guessed_states_len}/50 States Correct", "Enter state:").title()

    if answer_state in ["Exit", "Stop", "Give Up"]:
        for state in data.state.to_list():
            if state not in guessed_states:
                x = data[data.state == state]["x"].item()
                y = data[data.state == state]["y"].item()
                State(state, x, y, "red")
            screen.update()
        break

    if answer_state in data.state.to_list() and answer_state not in guessed_states:
        x = data[data.state == answer_state]["x"].item()
        y = data[data.state == answer_state]["y"].item()
        guessed_states.append(answer_state)
        State(answer_state, x, y)
        scoreboard.increase_score()
        screen.update()

    if guessed_states_len == 50:
        is_game_on = False

screen.exitonclick()
