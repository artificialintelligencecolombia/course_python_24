from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPEED_VALUES = [3, 4, 5]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.seth(180)
        self.penup()
        # Generate a y-coordinate in steps of 20 pixels within the range of -250 to 250
        y_pos = random.choice(range(-250, 251, 20)) 
        # Generate a random color from the list for each car object created
        random_color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.color(random_color)
        self.setpos(300, y_pos)
        self.speed = SPEED_VALUES[random.randint(0,len(SPEED_VALUES) - 1)]
        
    # Create the function that moves the car
    def drive(self):
        self.forward(self.speed)
        
    def increase_speed(self):
        self.speed += MOVE_INCREMENT