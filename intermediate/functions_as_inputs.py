# Higher order functions are functions that can work with another functions
# Here are the functions that will be called as parameters
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Higher order function:
def calculator(a,b, function):
    return function(a,b)

