line1 = ["[ ]", "[ ]", "[ ]"]
line2 = ["[ ]", "[ ]", "[ ]"]
line3 = ["[ ]", "[ ]", "[ ]"]

treasure_map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.\n")
print("     A      B      C")
print(f"1 {line1}\n2 {line2}\n3 {line3}\n")

position = input("Whete to put the treasure? ").lower()

abc = ["a", "b", "c"]
letter_index = abc.index(position[0])
number_index = int(position[1]) - 1

treasure_map[number_index][letter_index] = "[X]"

print("")
print("     A      B      C")
print(f"1 {line1}\n2 {line2}\n3 {line3}\n")
