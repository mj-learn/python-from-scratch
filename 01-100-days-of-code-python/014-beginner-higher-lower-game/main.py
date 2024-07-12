# FAQ: Why does choice B always become choice A in every round, even when A had more followers?
#
# Suppose you just started the game and you are comparing the followers
# of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers,
# so choice A is correct. However, the subsequent comparison should be between
# Selena Gomez (the new A) and someone else. The reason is that everything in our
# list has fewer followers than Instagram. If we were to keep Instagram as part of
# the comparison (as choice A) then Instagram would stay there for the rest of the game.
# This would be quite boring. By swapping choice B for A each round,
# we avoid a situation where the number of followers of choice A keeps going up
# over the course of the game. Hope that makes sense :-)

import random

from art import logo, vs
from data import data

print(logo)


def print_compare_list(compare_list):
    print(
        f"\n Compare A: {compare_list[0]["name"]}, a {compare_list[0]["description"]}, from {compare_list[0]["country"]}"
    )
    print(vs)
    print(
        f"\n Compare B: {compare_list[1]["name"]}, a {compare_list[1]["description"]}, from {compare_list[1]["country"]}\n"
    )


def check_answer(compare_list, guess):
    a = compare_list[0]["follower_count"]
    b = compare_list[1]["follower_count"]
    if a > b:
        correct = "a"
    else:
        correct = "b"

    if correct == guess:
        return True

    return False


def higher_lower_game():
    score = 0
    is_correct = True
    compare_list = random.choices(data, k=2)

    while is_correct == True:
        compare_list = [compare_list[1], random.choice(data)]

        while compare_list[0] == compare_list[1]:
            compare_list = [compare_list[0], random.choice(data)]

        print_compare_list(compare_list)

        guess = ""
        while guess not in ["a", "b"]:
            guess = input(" Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = check_answer(compare_list, guess)
        if is_correct:
            score += 1
            print(f" You're right! Current score: {score}")

    print(f"\n Sorry, that's wrong. Final score: {score}")


higher_lower_game()
