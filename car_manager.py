from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def cars_move(self):
        len_of_cars = len(self.all_cars)
        for num in range(0, len_of_cars):
            self.all_cars[num].forward(MOVE_INCREMENT)

    def collides(self, player):
        len_of_cars = len(self.all_cars)
        for num in range(0, len_of_cars):
            if player.distance(self.all_cars[num]) < 17:
                return True

    def car_spawn(self):
        car_color = choice(COLORS)
        car_y = randint(-250, 250)
        car = Turtle("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.setheading(180)
        car.color(car_color)
        car.goto(300, car_y)
        self.all_cars.append(car)
