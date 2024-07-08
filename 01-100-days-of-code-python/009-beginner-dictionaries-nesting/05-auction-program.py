logo = '''
    ___________
    \\         /
     )_______(
     |"""""""|_.-._,.---------.,_.-._
     |       | | |               | | ''-.
     |       |_| |_             _| |_..-'
     |_______| '-' `'---------'` '-'
     )"""""""(
    /_________\\
  .-------------.
 /_______________\\
'''
print(f"{logo}\n Welcome to the secret auction program.")

# Validation is not part of this exercise


def user_input():
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")  # not yet shown how to validate this
    return {"Name": name, "Bid": int(bid)}


def who_win(data):
    bid = 0
    winner = {}
    for bidder in data:
        if bid == 0:
            bid = bidder["Bid"]
            winner = bidder
        elif bid < bidder["Bid"]:
            winner = bidder
    print(f"The winner is {winner["Name"]} with a bid of ${winner["Bid"]}")


def auction_program():
    auction_data = []
    auction = ""

    while auction != "no":
        if len(auction_data) > 0 and auction != "yes":
            auction = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        else:
            auction_data.append(user_input())
            auction = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    who_win(auction_data)


auction_program()
