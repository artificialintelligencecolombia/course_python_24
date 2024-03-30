# Create a calculator
# 1. Usr inputs the first number
# 2. Program shows the operations and ask the usr to pick one
# 3. usr inputs the second number
# 4. Program prints the results
# 5. Program asks if usr wants to continue operation or finish the program

# 1. Define the operations of the calculator as functions and store the names of
# the operations and their keys 

# Function to add two numbers
def add(x, y):
    """Add Function"""
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    """Subtract Function"""
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    """Multiply Function"""
    return x * y

# Function to divide two numbers
def divide(x, y):
    """Divide Function"""
    if y == 0:  # Prevent division by zero
        return "Error! Division by zero."
    else:
        return x / y

operation_list= {
    "+": add, 
    "-": subtract, 
    "*": multiply,
    "/": divide
    }
# Functions can be used as values in a dictionary

def calculator():
    # 2. Program asks the first number
    num1 = int(input("Enter the first number: "))

    # 3. Program displays the operations and ask for choosing one
    for symbol in operation_list:
        print(symbol)

    # 6. While loop for continue calculations
    should_continue = True

    while should_continue:
        operator = input("Pick the operation: ")
        # 4. Program asks the second number
        num2 = int(input("Enter the second number: "))

        # Call the function from the dictionary according the user choice
        calculation_function = operation_list[operator] # store the function reference in 'calculation_function'
        result = calculation_function(num1,num2) # calls the function chosen by usr
        # This avoids the if/else statements

        # 5. Print the results
        print(f"{num1} {operator} {num2} = {result}")
        
        # 7. Ask the user if continue operating
        usr_answers = {
            "y": True,
            "n": False
        }
        
        user_continues = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation (y/n): ")
        continue_operation = usr_answers[user_continues]
        
        if continue_operation:
            num1 = result
        else:
            should_continue = False 
            calculator() # Recursion: when a function calls itself

calculator()