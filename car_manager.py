import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = .5
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 1
        self.car_movement_speed = self.calculate_car_movement_speed()
        for _ in range(20):
            self.generate_car()

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.car_movement_speed, car.ycor())
            if car.xcor() < -320:
                car.goto(320, car.ycor())

    def generate_car(self):
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(1, 2)
        car.goto(random.randint(-300, 320), random.randint(-12, 14) * 20)
        self.cars.append(car)

    def increase_difficulty(self):
        self.level += 1
        self.car_movement_speed = self.calculate_car_movement_speed()

    def calculate_car_movement_speed(self):
        return STARTING_MOVE_DISTANCE * self.level * MOVE_INCREMENT
