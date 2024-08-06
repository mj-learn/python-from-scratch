def positional_arguments(x, y, z):
    print(f"{x, y, z = }")


# positional_arguments(z=5, 2, x=8) # Error
positional_arguments(1, z=5, y=10)  # Output: 1, 10, 5  --> Correct


# def optional_arguments(x=5, y, z) # Error
def optional_arguments(x, y=5, z=8):
    print(f"{x, y, z = }")


optional_arguments(4, 4, 4)  # Output: 4, 4, 4
optional_arguments(4)  # Output: 4, 5, 8


def arbitrary_positional_arguments(x, y, *args):
    print(f"{x, y = }")
    print(f"{args = }")  # Tuple
    print(f"{type(args) = }")
    for arg in args:
        print(arg)


arbitrary_positional_arguments(22, 33, 1, 2, 3, 4, 5, 6, 7)
arbitrary_positional_arguments(22, 33, *[1, 2, 3, 4, 5, 6, 7])
arbitrary_positional_arguments(*[11, 22, 33, 1, 2, 3, 4, 5, 6, 7])


def arbitrary_keyword_arguments(x, y, **kwargs):
    print(f"{x, y, = }")
    print(f"{type(kwargs)}")  # Dictionary
    for key, value in kwargs.items():
        print(f"{key} = {value}")


arbitrary_keyword_arguments(33, 44, a=1, b=2, c=3, d=4)
arbitrary_keyword_arguments(*[33, 44], **{"a": 1, "b": 2, "c": 3, "d": 4})


def example_function(x, y, z=88, *args, **kwargs):
    print(f"{x, y, z = }")
    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


example_function(55, 66, 1, 2, 3, 4, 5, name="Alice", age=30)
example_function(55, 66, *[1, 2, 3, 4, 5], **{"name": "Alice", "age": 30})
