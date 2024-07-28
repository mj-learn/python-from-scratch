import random
from turtle import Turtle

COLORS = ["red", "orange", "green", "blue", "violet"]


class Traffic:
    def __init__(self):
        self.traffic = []
        self.speed = 5

    def create_car(self):
        random_chance = random.randint(1, 7)
        if random_chance == 1:
            new_y = random.randrange(-200, 220, 40)
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(320, new_y)
            self.traffic.append(new_car)

    def move_cars(self):
        for car in self.traffic:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += 2

    def is_collided_with(self, a):
        for car in self.traffic:
            if abs(a.xcor() - car.xcor()) < 30 and abs(a.ycor() - car.ycor()) < 20:
                return True
