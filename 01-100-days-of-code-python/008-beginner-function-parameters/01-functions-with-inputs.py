# Simple Function
def greet():
    print("Hello")
    print("how do you do?")
    print("Isn't the weather nice today?")
    print()


# Function that allows for input
def greet_with_name(name):  # name is parameter to function
    print(f"Hello {name}")
    print("how do you do?")
    print()


# Function that allows for input
def greet_with(name, location):  # name, location are parameters to function
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    print()


greet()

greet_with_name("mOnjofn")  # "mOnjofn" is argument to function (actual peace of data)

greet_with_name("Billie")  # "Billie" is argument to function

greet_with("mOnjofn", "Github.com")  # "mOnjofn", "Github.com" are arguments to function (actual peace of data)

greet_with("Microsoft", "Bill")  # Order is important [Positional Argument]

# Keyword Arguments
greet_with(location="Python", name="Guido")  # Order is not important [Keyword Arguments]
