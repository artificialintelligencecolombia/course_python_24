# Create the scoreboard class that keep count of the score for each snake feed.

from turtle import Turtle, Screen

# Create the constants of the scoreboard class
ALINGMENT = "center"
FONT = ("Arial", 19, "normal")

# Food class is going to inherit attrs and methods from the Turtle class
class Scoreboard(Turtle):
    def __init__(self):
        # Call the constructor of the parent class (Turtle)
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    
    # Create the method that updates the scoreboard
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)
    
    # Create a method that increases the score    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()