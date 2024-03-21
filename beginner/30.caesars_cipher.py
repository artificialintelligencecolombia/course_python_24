# Caesar's cipher.
#
# 1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# 2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
# e.g. 
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"
# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
# 
# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# 3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
 
from cipher_characters import latin_characters

# User parameters
#usr_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
usr_text = input("Type your message:\n")
usr_shift = int(input("Type the shift number:\n"))

# For wraping purposes, we need to know the length of the characters list
characters_len = len(latin_characters) # 95

# 'encrypt' function definition with parameters.
def encrypt(text, shift):
    # Hold the encrypted text into a new string.
    encrypted_text = ""
    # Iterate over each character of the usr_text.
    for char in text:
        # Check if current char is in the list.
        if char in latin_characters:
            # Calculate the new index for the char. '%' operation is used for wrapping around if shift exceeds the length of the list.
            new_index = (latin_characters.index(char) + shift) % characters_len
            # Add the new character (from the new index) to the encrypted_text.
            encrypted_text += latin_characters[new_index]
        else:
            # If char is not in latin list, add it unchanged to the encrypted_text.
            encrypted_text += char
    # Return the string encrypted
    return encrypted_text

# Calling of the encrypt function.
encrypted_text = encrypt(usr_text,usr_shift)

print("Original: ", usr_text)
print("Encrypted: ", encrypted_text)