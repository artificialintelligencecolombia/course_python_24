# Create the food class that renders itself as a small cirlce (form) and to move to a new location each time the snake(head) touches the food

from turtle import Turtle, Screen

# Food class is going to inherit attrs and methods from the Turtle class
class Food(Turtle):
    def __init__(self):
        # Call the constructor of the parent class (Turtle)
        super().__init__() 
        self.shape("circle") # Sets the shape of the Food object to a circle. Using 'self' to set properties on the current instance.
        self.penup()  # Make sure the food doesn't draw when it moves
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Reduces the food object size to half
        self.color("blue")
        self.speed("fastest")  # Set the speed to the fastest for quick positioning
        self.refresh()  # Call a method to place the food at a random position
        # Note: all this methods come from Turtle class
    
    def refresh(self):
        """Move the food to a random location on the screen."""
        import random
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)
        