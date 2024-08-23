try:
    # Her goes the code that might throw and exception (error) -> If error occurs, the flow is transferred to the 'except' block.
    pass

except:
    # This block handles the error gracefully instead stopping the program abruptly. Here we can specify different types of exceptions to handle specific errors. Catch is the equivalent of 'except'.
    pass

else:
    # (optional) This block is executed only if no exceptions were raised in the 'try' block.
    pass

finally:
    # (optional) This block is always executeed, regardless of whether an exception occurred or not.
    pass
    