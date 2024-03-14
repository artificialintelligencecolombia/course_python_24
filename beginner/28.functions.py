# Function are implemented when we want to re use
# a piece of code
def my_function():
    print("hello hacker, from function")

# Calling the function to be executed
my_function()

# Function with inputs: We can input data into 
# the function for using it in the function's code.
def greet_with_name(name):   
    print(f"Hello {name}.")
# 'name' is a variable -> parameter

greet_with_name("Daniel") 
greet_with_name("Juana")
# Danil & Juana are called function's arguments

# Multiple inputs
def where_are_you(name, location):
    print(f"Ey {name}. I've heard you're in {location}")

# Positional arguments needs to be in the defined order
# as the parameters when the function was created.
where_are_you("Omer", "Santa Marta")

# Keyword arguments defines the parameters and its
# arguments aside, so we can input them in any given
# order.
where_are_you(location="Peru", name="Sofia")
# The arguments are in different order, yet it works

