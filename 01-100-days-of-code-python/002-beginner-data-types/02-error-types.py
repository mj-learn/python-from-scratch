# TypeError
num_char = len(input("What is your name? "))

# print("Your name has " + num_char + " characters.") # TypeError: can only concatenate str (not "int") to str

a = "123"
print(type(a))

a = int(a)  # Convert a to string
print(type(a))

a = float(a)  # Convert a to float
print(type(a))

# Autoconvert int to float
print(70 + float("100.5"))

# Exercise to print length of name

print(type(num_char))  # Print the type of num_char

new_num_char = str(num_char)  # Convert num_char to string

print("Your name has " + new_num_char + " characters.")
