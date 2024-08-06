# FUNCTION WITH FLEXIBLE NUMBER OF ARGUMENTS
# To create a flexible function that can accept any number of arguments, we use the '*' symbol.
# This symbol allows us to pass a variable number of non-keyword arguments to the function.
# The arguments are stored in a tuple named 'args'.

def add(*args): # function accepts any number of positional arguments
    sum = 0
    for n in args:
        sum += n
    print(type(args)) # being a tuple, we can use indexing -> args[2]: 87
    # print(args[2])
    return sum

print(add(1,2,3,4)) # o: 10
print(add(10,5,87,1,3,9,14,4,58,7,5,32)) # o: 235



# FUNCTION WITH FLEXIBLE NUMBER OF KEYWORD ARGUMENTS
# To create a flexible function that can accept UNLIMITED number of keyword arguments, we use the '**' symbol _> It allows us to pass a variable number of keyword arguments to the function.
# The arguments are stored in a dictionary named 'kwargs'.

def calculate(n, **kwargs): # function accepts any number of keyword arguments
    #print the key, value pairs of the kwargs dictionary
    for key,value in kwargs.items():
        print(f"{key}={value}")
        
    n += kwargs.get('add', 0)        # default value is 0 if 'add' is not provided
    n *= kwargs.get('multiply', 1)   # default value is 1 if 'multiply' is not provided
    # If the key is not present in the dictionary, .get() returns a default value which you can specify.
    return n

print(calculate(2)) # o: 2 -> No keyword arguments
print(calculate(2, add=3)) # o: 5 -> missing keyword arguments
print(calculate(2, add=3, multiply=4))  # Output: 20


# **KWARGS IN CLASSES
class Person:
    def __init__(self, name, **kwargs): # the object accepts any number of arguments
        # Required attribute
        self.name = name
        # Optional attributes with defaults using .get()
        # If we don't specify the following attributes, by using .get() they will either take their default values or be ignored if no default is provided, BUT THEY WONT RETURN ERROR (GOOD!)
        self.age = kwargs.get('age', None)
        self.city = kwargs.get('city')
        self.occupation = kwargs.get('occupation', 'Unemployed')
        self.hobby = kwargs.get('hobby', 'None')
        
person1 = Person(name='John') # Providing only the required attribute

print(person1.name) # o: John
print(person1.city) # o: None

# **kwargs in Classes: Allows the class constructor to accept a flexible number of keyword arguments.
# Using .get() Method: Ensures safe access to dictionary values with defaults, preventing errors if the key is not present.
# Default Values: Provides default values for optional attributes, making the class robust and flexible in handling varying inputs.