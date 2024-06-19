# Import required library
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

# Constants
USR_PADDLE_POSITION_X = -380

# Set up the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
# screen.tracer(0)  # Stops the window from updating automatically

# Create the paddles & ball 
usr_paddle = Paddle((USR_PADDLE_POSITION_X,0)) # Left paddle at (-380, 0)
second_paddle = Paddle((-USR_PADDLE_POSITION_X,0)) # Right paddle at (380, 0)
ball = Ball()

# Enable key event listening 
screen.listen()

# Binding arrow keys to the usr paddle's move_ methods
screen.onkey(usr_paddle.move_up, "w")
screen.onkey(usr_paddle.move_down, "s") 
screen.onkey(second_paddle.move_up, "Up")
screen.onkey(second_paddle.move_down, "Down") 

# Create the token for the snake movement
game_is_on = True
# Main game loop
while game_is_on:
    # screen.update()  # Manually update the screen 
    ball.move()
    
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

# Close the window on click
screen.exitonclick()
