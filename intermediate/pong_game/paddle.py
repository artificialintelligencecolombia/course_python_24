# Create the class 'paddle' for the game.

# Import required packages/modules
from turtle import Turtle

class Paddle():
    def __init__(self, position): # constructor method. Initialize the paddle at a specified position
        self.create_paddle(position)
      
    def create_paddle(self, position):
        self.paddle = Turtle() # Create a turtle object for the paddle
        self.paddle.speed(0) # Set the speed to the maximum (no animation delay)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=3, stretch_len=2)
        self.paddle.penup() # Set the speed to the maximum (no animation delay)
        self.paddle.goto(position) # Move the paddle to the specified position
    
    # Functions to move the paddle vertically    
    def move_up(self):
        # Move the paddle up by 20 pixels
        y = self.paddle.ycor() # Get current y-coordinate
        y += 20 # Increase y-coordinate
        self.paddle.sety(y) # Set new y-coordinate
        
    def move_down(self):
        # Move the paddle down by 20 pixels
        y = self.paddle.ycor()  # Get current y-coordinate
        y -= 20  # Decrease y-coordinate
        self.paddle.sety(y)  # Set new y-coordinate
