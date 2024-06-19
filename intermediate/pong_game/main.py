# Import required library
from turtle import Turtle, Screen
from paddle import Paddle

# Constants
USR_PADDLE_POSITION_X = -380

# Set up the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
# window.tracer(0)  # Stops the window from updating automatically

# Create the paddle 
usr_paddle = Paddle((USR_PADDLE_POSITION_X,0)) # Left paddle at (-380, 0)
second_paddle = Paddle((-USR_PADDLE_POSITION_X,0)) # Right paddle at (380, 0)

# Enable key event listening 
screen.listen()

# Binding arrow keys to the usr paddle's move_ methods
screen.onkey(usr_paddle.move_up, "Up")
screen.onkey(usr_paddle.move_down, "Down") 
screen.onkey(second_paddle.move_up, "o")
screen.onkey(second_paddle.move_down, "l") 

# Close the window on click
screen.exitonclick()