# Import required library
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

# Constants
LEFT_POSITION_X = -380
RIGHT_POSITION_X = 380

# Screen set up
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Stops the window from updating automatically

# Create the paddles & ball 
left_paddle = Paddle((LEFT_POSITION_X,0)) # Left paddle at (-380, 0)
right_paddle = Paddle((RIGHT_POSITION_X,0)) # Right paddle at (380, 0)
ball = Ball()

# Event binding for paddle movement 
screen.listen()

# Binding arrow keys to the usr paddle's move_ methods
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s") 
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down") 

# Create the token for the snake movement
game_is_on = True

# Game loop
while game_is_on:
    screen.update()  # Manually update the screen 
    ball.move()
    
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
        
    # Detect collision with the paddles
    if ball.distance(left_paddle.paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    
    if ball.distance(right_paddle.paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    
    if ball.xcor() > 360:
        ball.reset_position()
    
# Close the window on click
screen.exitonclick()
