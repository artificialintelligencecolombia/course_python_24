# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they
# will turn 100 years old.
#
# EXTRAS: 
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)}

# Import date module
from datetime import datetime

# Storing current year in a variable
current_year = datetime.now().year
# print(current_year) -> testing

name = input("Hello user. Enter your name: ")
age = int(input("Enter your age: " ))
repetitions = int(input("Enter a number of repetitions for the message: "))

for i in range(repetitions):
    print(f"{name} will reach 100 years old in {current_year + (100 - age)}.")
