"""
Higher-order functions are functions that can take other functions as arguments or return them as results.
They are a powerful feature in Python and many other programming languages, enabling more flexible and reusable code.
Common examples of higher-order functions include 'map', 'filter', and 'reduce',
as well as user-defined functions that operate on other functions.
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def calculator(x, y, func):  # higher order function
    return func(x, y)


result = calculator(1, 2, add)
print(result)

result = calculator(1, 2, subtract)
print(result)

result = calculator(1, 2, multiply)
print(result)

result = calculator(1, 2, divide)
print(result)
