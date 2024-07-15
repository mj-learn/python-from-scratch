from turtle import Screen, Turtle

# All classes are named in PascalCase

bob = Turtle()  # bob is a object, Turtle is a class
bob.shape("turtle")  # shape is a method of the object bob
bob.color("coral")
bob.forward(100)

my_screen = Screen()
my_screen.exitonclick()

# turtle is part of Python Standard Library like random, math, etc ...
# if we want to install other python packages need to use pip or conda
