# Bring in the imports needed
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creates the main screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Generates the objects from our classes
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Gets the screen ready
screen.listen()
screen.onkey(player.move, "Up")

# Tracks the game
game_is_on = True

# Main loop for the game
while game_is_on:

    # Keeps the screen updated
    time.sleep(0.1)
    screen.update()
    car_manager.engines_on()

    # places cars at new positions when they get to the end of the screen
    for car in car_manager.cars:
        if car.xcor() < -310:
            car_manager.new_position(car)

    # Levels up if player reaches the other side of the street
    if player.ycor() > 300:
        player.reset_position()
        scoreboard.go_up_level()
        car_manager.increase_speed()

    # Ends the game if the player gets hit by a car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

# Closes the screen on a click
screen.exitonclick()
