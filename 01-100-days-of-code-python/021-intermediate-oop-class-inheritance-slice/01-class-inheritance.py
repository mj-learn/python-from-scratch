# Class inheritance in Python allows a class (child) to inherit attributes and methods from another class (parent).
# It promotes code reuse and establishes a relationship between the parent and child classes.
# The child class can override or extend the functionalities of the parent class.


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this with air")


class Fish(Animal):

    def swim(self):
        print("Moving in water.")

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")


doggo = Dog()
doggo.breathe()

print()

nemo = Fish()
print(nemo.num_eyes)
nemo.breathe()
