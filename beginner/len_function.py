# len() function counts the number of chars in a string
# str() function parses a number data typa to a string, as the input's a number 
# type() function retrieves the data type of any variable
print("Your last name contains " + str(len(input("What's your last name?"))) + " characters.")

first_name = input("What's your first name?")
name_length = len(first_name)
print(first_name + " is composed of " + str(name_length) + " characters.")

# Note: empty spaces "_" are string elements as well. They count as characters 

print(type(True)) # <class 'bool'>
print(type([7,'hello', False])) # <class 'list'>