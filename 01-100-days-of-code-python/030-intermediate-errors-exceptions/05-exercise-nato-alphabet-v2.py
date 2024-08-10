import pandas

data = pandas.read_csv("05-nato_phonetic_alphabet.csv")

print("Welcome to NATO Alphabet Project")
print("Type: [stop, exit, close] to end the program")


while True:
    try:
        user_input = input("\nEnter a single word: ").upper()

        if user_input in ["STOP", "EXIT", "CLOSE"]:
            break

        nato = [data[data.letter == char].code.item() for char in user_input]
    except ValueError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato)
