# The program will generate a password according to the user's requirements.
# User will input the number of characters: from 16 to 24. The characters could
# be any combination of upper and lower case.
# The user will input the number of numbers in the password: from 0 to 9
# The user will input the number of special characters for the password.

# Required libraries
import random
import string

# create the total of existing characters from the librariy and store them
# in the instance 'characters'.

# -> Checking the characters used.
# print(string.ascii_letters + string.punctuation + string.digits)

characters = string.ascii_letters + string.punctuation + string.digits

# As list1 = [] for example, we can create a string instance password = "".
# password will contain the characters.
password = ""

# Provide the password_length
password_length = random.randint(8,16)

for x in range(password_length):
    char = random.choice(characters) # .choice() returns a random choice.
    password += char    # No need to .append() as lists, just "+".
print(password)
    