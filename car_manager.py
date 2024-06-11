# Grab imports
from turtle import Turtle
import random

# Initialize constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Create the Car Manager Class
class CarManager:
    # Create the starting properties
    def __init__(self):
        # super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.starting_cars()

    # Method for creating a new car
    def new_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(random.randint(-280, 280), random.randint(-260, 280))
        self.cars.append(new_car)

    # Method for randomly placing a car at a new position
    def new_position(self, current_car):
        new_position = (305, random.randint(-260, 280))
        current_car.goto(new_position)

    # Method to generate the starting set of cars
    def starting_cars(self):
        for i in range(15):
            self.new_car()

    # Method for making the cars move accross the screen
    def engines_on(self):
        for car in self.cars:
            car.forward(self.speed)

    # Method for increasing speed as the level goes up
    def increase_speed(self):
        self.speed += MOVE_INCREMENT