# Create the class 'paddle' for the game.

# Import required packages/modules
from turtle import Turtle

# Create the constants used in the object class
USR_PADDLE_POSITION_X = 380

class Paddle():
    def __init__(self):
        self.create_paddle()
        
    def create_paddle(self):
        # Create the paddle
        paddle = Turtle()
        paddle.speed(0)
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=3, stretch_len=2)
        paddle.penup()
        paddle.goto(USR_PADDLE_POSITION_X, 0)