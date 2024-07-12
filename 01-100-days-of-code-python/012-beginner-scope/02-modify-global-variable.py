# Modifying Global Scope
number = 5


def increase_number_bad():
    # It's bad practise to modify like this
    global number
    number += 3
    print(f"number inside function: {number}")


def increase_number_correct():
    return number + 1


number = increase_number_correct()


increase_number_bad()
print(f"number outside function: {number}")
