# The program will execute a function that checks if the number that a user inputs is a prime number.

# User inputs the number
print("\nPRIME NUMBER CHECKER!\n")
user_number = int(input("Please enter a nunber: "))

# Function definition, including parameter
def prime_check(number):
    # Conditional for checking the number status
    if number < 2:
        return False
    else:
        for i in range (2, int(number**0.5)):
            if number % i == 0:
                return False
        return True
            
# Calling the function
result = prime_check(user_number)

# Print validation or negative for the number
if result == False:
    print(f"{user_number} is not a prime number.")
else:
    print(f"{user_number} is a prime number.")

