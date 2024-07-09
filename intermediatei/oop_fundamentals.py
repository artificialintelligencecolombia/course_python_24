# We can call a class method from a module
from turtle import Turtle, Screen # module | class(es)

# Create the instance of the class
my_turtle = Turtle() # Initialize/Construct the obj from class
my_screen = Screen() # Initialize another obj

# Printing obj
print(my_turtle) 
# output: <turtle.Turtle object at 0x000002AED8C56000>
# output: obj instance | memory address where the object is stored

# Calling attributes
height_attr = my_screen.canvheight # obj.attr
print(height_attr) # output: 300 is the value of the attr

# Call the obj methods
my_turtle.shape("triangle")
my_turtle.forward(150)  
my_turtle.color("green")
my_screen.exitonclick()
