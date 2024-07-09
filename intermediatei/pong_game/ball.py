# Create the ball class that renders itself as a small cirlce (form).

from turtle import Turtle

# Ball class is going to inherit attrs and methods from the Turtle class
class Ball(Turtle):
    def __init__(self):
        # Call the constructor of the parent class (Turtle)
        super().__init__()
        self.speed(6)  # Set the speed of animation
        self.shape("circle") # Sets the shape of the Ball object to a circle. Using 'self' to set properties on the current instance.
        self.color("white")
        self.penup()  # Make sure the ball doesn't draw when it moves
        self.goto(0,0)
        self.x_move = 10  # Initial movement in the x-direction
        self.y_move = -10  # Initial movement in the y-direction
    
    def move(self):
        # Calculate the new position
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)  # Move the ball to the new position
        
    def wall_bounce(self):
        # Reverse the y-direction
        self.y_move *= -1
        
    def bounce_x(self):
        # Reverse the y-direction
        self.x_move *= -1    
    
    def reset_position(self):
        # Move the ball back to the center and reverse the x-direction
        self.goto(0, 0)
        self.bounce_x()