# The script will check if a number (user's input) is even or odd. The it will
# print the message indicating the number's nature.

user_number = int(input('Please enter a number: '))

if user_number % 2 == 0:
    print(f"Your number is {user_number}. This is a EVEN number.")
else:
    print(f"Your number is {user_number}. This is a ODD number.")