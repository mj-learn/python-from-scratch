class Animal:
    def __init__(self, animal_name):
        self.name = animal_name

    def speak(self):
        print(f"{self.name} says: ", end="")


class Dog(Animal):
    def __init__(self, dog_name):
        dog_name = dog_name.upper()
        super().__init__(dog_name)
        self.num_of_eyes = 2

    def speak(self):
        super().speak()
        print("woof woof")

    def bark(self):
        super().speak()
        print("bark bark")


class Cat(Animal):
    def __init__(self):
        self.num_of_paws = 4

    def speak(self):
        print("meow meow")


class Fish(Animal):
    def swim(self):
        print("Doing this underwater.")


class GoldFish(Fish):
    def speak(self):
        super().speak()
        print("money money")

    def swim(self):
        super().swim()
        print("And shine in gold.")


doggo = Dog("Guido")
print(doggo.name)  # Output: GUIDO
print(doggo.num_of_eyes)  # 2
doggo.speak()  # Output: GUIDO says: woof woof
doggo.bark()  # Output: GUIDO says: bark bark

print()

kitty = Cat()
# print(kitty.name)  # Output: Error (Missing name attribute)
print(kitty.num_of_paws)  # Output: 4
kitty.speak()  # meow meow meow meow meow meow meow

print()

nemo = Fish("Nemo")
print(nemo.name)  # Output: Nemo
nemo.speak()  # Output: Nemo says:
nemo.swim()  # Output: Doing this underwater.

print()

trump = GoldFish("Trump")
print(trump.name)
trump.speak()
trump.swim()
