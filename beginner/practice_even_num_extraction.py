# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write a script of Python that takes this list a and makes a new list that has only the even 
# elements f rom the list.

# Required libraries
import random

# Define the variables for the list length and the list itself.
list_length = int(input("Define the list length: "))
numbers_list = []

# Append the numbers generated randomly to the list.
for i in range(list_length):
    number = random.randint(0, 100)
    numbers_list.append(number)

# Display the list                  
print(f"\nThe list created: %s" % numbers_list)

# Filter even numbers from the original list and create a new list
even_numbers_list = []
for number in numbers_list:
    if number % 2 == 0:
        even_numbers_list.append(number)
# even_numbers_list = [num for num in numbers_list if num % 2 == 0]
# CODE ABOVE IS AN ALTERNATIVE
        
# Print the resulting list
print(f"\nEven numbers list:\n")
print(even_numbers_list)
