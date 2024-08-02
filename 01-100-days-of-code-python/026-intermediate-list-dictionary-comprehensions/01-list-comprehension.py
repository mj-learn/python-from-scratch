# new_list = [new_item for item in some_list]
numbers = [1, 2, 3]

# With no comprehension
new_list = []
for item in numbers:
    add_1 = item + 1
    new_list.append(add_1)

print(f"{new_list = }")

# With comprehension
new_list_comprehension = [item + 1 for item in numbers]
print(f"{new_list_comprehension = }")


def char_plus_a(char):
    return char + "a"


some_string = "Guido"
char_list = [char_plus_a(character) for character in some_string]
print(f"{char_list = }")

# Create a new list from a range, where the list items are double the values in the range
challenge_1 = [num * 2 for num in range(1, 5)]
print(f"{challenge_1 = }")

# new_list = [new_item for item in some_list if test]
persons = ["Guido", "Angela", "Linus", "Mitnick", "wall-e", "EVE", "mOnjofn", "Dexter", "Dee Dee", "Satoshi"]
beautiful_and_rich = [person for person in persons if person.startswith("A") or person.endswith("n")]
print(f"{beautiful_and_rich = }")
