# Create the class snake for the game.

# Import required packages/modules
from turtle import Turtle

# Create the constants used in the object class
START_POSITIONS_XAXIS = [0, -20, -40] # Initial positions for the snake segments
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake_body = []
        self.create_snake() # Create the snake once the object is instantiated
        
    def create_snake(self):
        # Create the initial snake body with 3 segments
        for i in range(0, 3):  # Three turtle objects
            new_turtle = Turtle()
            new_turtle.shape("square") 
            new_turtle.color("white") # Those are all the turtle's settings.
            new_turtle.penup() # Prevent the turtle from drawing when moving
            new_turtle.setposition(START_POSITIONS_XAXIS[i], 0)
            self.snake_body.append(new_turtle)   
            
    def move(self):
        # Iterate over the snake body segments from the last segment (tail) to the second segment. 
        for segment in range(len(self.snake_body)-1, 0, -1): # From the last segment to the first segment (excluding the head)
            # Get the x,y-coordinates of the previous segment
            new_x = self.snake_body[segment-1].xcor() 
            new_y = self.snake_body[segment-1].ycor()
            # Move the current segment to the position of the previous segment
            self.snake_body[segment].goto(new_x,new_y) 
        self.snake_body[0].forward(DISTANCE)
        
    def move_up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)
        
    def move_down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)
    
    def move_left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)
    
    def move_right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)   