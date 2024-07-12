from art import logo

print(logo)

# data validation is not part of this exercise
# I know there are same build in functions


def _add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def add(n1, n2):
    return n1 + n2


def get_result(again, result):
    if again == "n":
        result = ""

    if result == "":
        first_number = float(input("What's first number?: "))
    else:
        first_number = result
        print(f"First number is {first_number}")

    operation = ""
    while operation not in ["+", "-", "*", "/"]:
        operation = input("Pick an operation (+, -, *, /): ")

    secound_number = float(input("What's the secound number?: "))

    result = calculate(operation)(first_number, secound_number)  # hah this works (I love python)
    result = round(result, 4)

    print(f"{first_number} {operation} {secound_number} = {result}\n")

    again = ""
    while again not in ["y", "n", "exit"]:
        again = input("Type 'y' to continue, type 'n' to start a new calculation, type 'exit' to exit: ")

    print()

    return [again, result]


def calculate(operation):
    operations = {
        "+": _add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    return operations[operation]


def calculator():
    result = ""
    again = ""

    while again != "exit":
        [again, result] = get_result(again, result)  # hah this works too (I love python)


calculator()
