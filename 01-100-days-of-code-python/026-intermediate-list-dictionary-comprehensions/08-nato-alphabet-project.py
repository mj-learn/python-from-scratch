import pandas

data = pandas.read_csv("08-nato_phonetic_alphabet.csv")
# print(data[data.letter == "B"].code.item())
# abc = ["A", "A", "F", "B", "C"]
# nato = [data[data.letter == char].code.item() for char in abc]
# print(nato)

print("Welcome to NATO Alphabet Project")
print("Type: [stop, exit, close] to end the program")

while True:
    user_input = input("\nEnter a single word: ").upper()

    if user_input in ["STOP", "EXIT", "CLOSE"]:
        break

    nato = [data[data.letter == char].code.item() for char in user_input]
    print(nato)
