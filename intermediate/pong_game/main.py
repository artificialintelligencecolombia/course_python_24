# Import required library
from turtle import Turtle, Screen
from paddle import Paddle

# Set up the screen
window = Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
# window.tracer(0)  # Stops the window from updating automatically

# Create the snake, food and score
right_paddle = Paddle()

# Close the window on click
window.exitonclick()