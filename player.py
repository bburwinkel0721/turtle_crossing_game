# Bring in imports
from turtle import Turtle

# Create constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Create the player class
class Player(Turtle):
    # Create the starting properties
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    # Method for allowing the player to move
    def move(self):
        self.forward(MOVE_DISTANCE)

    # Resets the players position after each round
    def reset_position(self):
        self.goto(STARTING_POSITION)