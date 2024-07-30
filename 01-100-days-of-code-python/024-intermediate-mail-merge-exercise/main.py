# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()

for name in names:
    new_letter = letter_template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(new_letter)
