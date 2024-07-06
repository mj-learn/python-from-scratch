import random

from hangman_art import logo, stages
from hangman_words import word_list


def choose_a_word(list_of_words):
    choosen_word = random.choice(list_of_words)
    return choosen_word


def create_guess_list(word):
    guess_list = []
    for _ in word:
        guess_list.append("_")
    return guess_list


def ask_user():
    print()
    answer = input(" Guess a letter: ").lower()
    return answer


def check_answer(user_guess, chosen_word, guess_list):
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            guess_list[position] = letter


def remove_live(user_guess, chosen_word, guesses_list, lives):
    if user_guess not in chosen_word or user_guess == "":
        print(f" You guessed {user_guess}, that's not in the word. You lose a life.")
        lives -= 1
    elif user_guess in guesses_list:
        print(f" You've already guessed {user_guess}")
    else:
        print(f" You guessed {user_guess}, that's in the word.")
    return lives


def is_word_guessed(guess_list):
    if "_" in guess_list:
        return "no"
    return "yes"


def display_guessed(guess_list):
    display = ""
    for char in guess_list:
        display += char + " "
    print(f"               {display}")


def print_status(guess_list, lives_left):
    print()
    if lives_left < 7:
        print(stages[lives_left])
    display_guessed(guess_list)
    print()
    print(f"               Lives left: {lives_left}")


def hangman():
    user_lives = 7
    end_of_game = "no"
    chosen_word = choose_a_word(word_list)
    guesses_list = create_guess_list(chosen_word)

    print(f"Pssst, the solution is: {chosen_word}")  # For debugging
    print(f"{logo}")
    print_status(guesses_list, user_lives)

    while user_lives != 0:
        user_guess = ask_user()
        user_lives = remove_live(user_guess, chosen_word, guesses_list, user_lives)
        check_answer(user_guess, chosen_word, guesses_list)
        print_status(guesses_list, user_lives)
        end_of_game = is_word_guessed(guesses_list)
        if end_of_game == "yes":
            break

    if user_lives > 0:
        print("\n                  You win!")
    else:
        print("\n                 You lose!")


hangman()
