# Types of errors

# 1. FileNotFound
# with open ("file_non_existent.txt") as f:
#   f.read()

# 2. KeyError
# a_dict = {"key": "value"}
# value = a_dic["another_key"]

# 3. IndexError
# fruits = ["Banana", "Apple"]
# fruit = fruits[3]

# 4. TypeError
# text = "abc"
# print(text + 5)

# 5. ValueError
# int("abc")  

# 6. AttributeError -> 'uppercase' is not a method of str
# text = uppercase("abc")

# 7. ImportError
# import non_existent_module  

# 8. ZeroDivisionError
# result = 10 / 0  

# 9. IndentationError
# def some_function():
# print("Hello")  

# 10. SyntaxError -> when there is an error in Python syntax.
# eval('x === x') 

# 11. NameError
# print(undeclared_variable)  

# 12. UnboundLocalError -> referencing a local variable before it has been assigned.
# def example():
#    print(x)
#    x = 10  

# 13. MemoryError
# Trying to create a very large object
# x = [1] * (10**10)  

# 14. OverflowError -> when the result of an arithmetic operation is too large to be expressed within the available range.
# import math
# math.exp(1000)  
