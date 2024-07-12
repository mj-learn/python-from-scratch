# Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

logo = """
   _____                     _                _____
  / ____|                   (_)              / ____|
 | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___
 | | |_ | | | |/ _ \\/ __/ __| | '_ \\ / _` | | | |_ |/ _` | '_ ` _ \\ / _ \\
 | |__| | |_| |  __/\\__ \\__ \\ | | | | (_| | | |__| | (_| | | | | | |  __/
  \\_____|\\__,_|\\___||___/___/_|_| |_|\\__, |  \\_____|\\__,_|_| |_| |_|\\___|
                                      __/ |
                                     |___/
    """

print(logo)
print(" Welcome to the Number Guessing Game!")
print(" I'm thinking of a number between 1 and 100.\n")

NUMBER = random.randint(1, 100)
print(f" Pssst, the correct answer is {NUMBER}\n")


def choose_difficulty():
    difficulty = ""
    while difficulty not in ["easy", "hard"]:
        difficulty = input(" Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return 10

    return 5


def guess_the_number():
    attempts = choose_difficulty()
    guess = int()

    print(f"\n You have {attempts} attempts remaining to guess the number.")

    while guess != NUMBER and attempts > 0:
        guess = int(input(" Make a guess: "))

        if guess > NUMBER:
            attempts -= 1
            print(" Too high.\n Guess again.")
        elif guess < NUMBER:
            attempts -= 1
            print(" Too low.\n Guess again.")

        if guess != NUMBER and attempts > 0:
            print(f"\n You have {attempts} attempts remaining to guess the number.")

    if guess == NUMBER:
        print(f"\n You got it! The answer was {NUMBER}.")
    else:
        print(f"\n You've run out of guesses, you lose. The answer is {NUMBER}.")


guess_the_number()
