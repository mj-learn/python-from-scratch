# Dictionaries
# Unordered Key:Value pairs: {"key":"value","name":"John"}

programming_dictionary = {
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    "Bug": "An error in a program that prevents the program from running as expected.",
}

# Retrieving items from dictionary
print(programming_dictionary["Function"])  # print value for "Function" key

# Creating empty dictionary
new_programming_dictionary = {}

# Adding new items to dictionary
new_programming_dictionary["Key"] = "Some value"

print(new_programming_dictionary)

# Wipe (clear) an existing dictionary
new_programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(new_programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")
