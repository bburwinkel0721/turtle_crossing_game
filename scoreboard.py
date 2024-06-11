# Bring in the imports
from turtle import Turtle

# Create the constants
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"

# Create the scoreboard class
class Scoreboard(Turtle):
    # Create the starting properties
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    # Raise the level on the scoreboard
    def go_up_level(self):
        self.level += 1
        self.score_update()

    # Updates the scoreboard with new info
    def score_update(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    # Ends the game and displays the end screen
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)