# FUNCTION WITHOUT DEFAULT ARGUMENTS
# When you call my_function, you must provide ALL arguments: my_function(1, 2, 3). If you try to call it with fewer than three arguments, Python will raise a TypeError.

def my_function(a,b,c):
    # do this with a
    # then do this with b
    # then do this with c
    pass

# my_function(1,2,3)

# FUNCTION WITH DEFAULT ARGUMENTS (KEYWORD ARGUMENTS)
# These functions have one or more parameters with default values. If I don't provide a value for these parameters when calling the function, the function uses the default values. 
# can call a function with arguments out of order by using keyword arguments.
def my_other_function(a,b=2,c=4):
    pass

my_other_function(a=1)
my_other_function(c=5,a=2)