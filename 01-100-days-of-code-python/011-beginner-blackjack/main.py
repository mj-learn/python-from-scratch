############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(list_of_cards):
    score = sum(list_of_cards)

    if 11 in list_of_cards and score > 21:
        score -= 10

    return score


def compute_strategy(computer_cards):
    while calculate_score(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
    return computer_cards


def print_cards(player_cards, computer_cards):
    print(f"\n Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
    print(f" Computer's first card: {computer_cards[0]}\n")


def print_final_result(player_cards, computer_cards):
    player_score = calculate_score(player_cards)
    compute_score = calculate_score(computer_cards)

    print(f"\n Your cards: {player_cards}, current score: {player_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {compute_score}\n")

    if player_score > 21:
        print("\n You went over. You lose 😭\n")
        return

    if compute_score > 21:
        print("\n You win! Opponent went over. 😁\n")
        return

    # blackjack player
    if player_score == 21 and len(player_cards) == 2:
        print("\n Win, you have Blackjack 😱")
        return

    # blackjack computer
    if compute_score == 21 and len(computer_cards) == 2:
        print("\n Lose, opponent has Blackjack 😱\n")
        return

    if player_score < compute_score:
        print("\n You lose 😭\n")
        return

    if player_score > compute_score:
        print("\n You win 😃\n")
        return

    if player_score == compute_score:
        print("\n Draw 🙃\n")


def blackjack():
    player_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)
    another_card = ""
    player_score = calculate_score(player_cards)

    print_cards(player_cards, computer_cards)

    while another_card != "n" and player_score <= 21:

        another_card = ""
        while another_card not in ["y", "n"]:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card == "y":
            player_cards.append(random.choice(cards))
            player_score = calculate_score(player_cards)
            if player_score <= 21:
                print_cards(player_cards, computer_cards)

    if player_score <= 21:
        computer_cards = compute_strategy(computer_cards)

    print_final_result(player_cards, computer_cards)

    play_or_not()


def play_or_not():
    play = ""
    while play not in ["y", "n"]:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play == "y":
        print()
        blackjack()


play_or_not()
