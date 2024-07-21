import turtle as t
import random

# Tuples: Ordered immutable sequence of objects: (10, "hello", 200.3, True)
# A tuple in Python is an immutable list that can contain different data types.
# It is defined using parentheses and is faster to work with compared to a list.
# Tuples are used to store collections of items that should not be changed.
# They support operations like indexing, slicing, and iteration.

my_tuple = (1, 2, 3)
print(my_tuple[0])
# my_tuple[2] = 5 # you can't add in, remove from or change tuples

# Convert tuple to a list
my_list = list(my_tuple)
print(my_list)


# Generate random RGB Colors using tuples
def randon_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Using random_rgb in turtle
t.colormode(255)


def random_walk():
    tim = t.Turtle()
    tim.speed(8)
    tim.pensize(15)

    for _ in range(300):
        tim.pencolor(randon_rgb())
        tim.forward(35)
        tim.setheading(random.choice([90, 180, 270, 360]))

    screen = t.Screen()
    screen.exitonclick()


random_walk()
