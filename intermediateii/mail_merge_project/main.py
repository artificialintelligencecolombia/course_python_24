#!usr/bin/env python3

import os # Handles file paths and dir operations.

# Set the filepaths and the modes
blueprint_filepath = './Input/Letters/starting_letter.txt'
list_of_invitees_filepath = './Input/Names/invited_names.txt'
blpnt_mode = 'r+'
invt_mode = 'r'
list_of_names = []
output_dir = './Output/ReadyToSend' # Where personalized messages will be saved.

# Fn that reads the files and returns the content -> str.
def read_file(filename, mode):
    try:
        with open(filename, mode) as file:
            # If blueprint file, we need to edit it.
            if mode == 'r+':
                content = file.read()
                return content
            # If the file is the name list, only read.
            if mode == 'r':
                lines = file.readlines()
                return [line.strip() for line in lines]       
    except FileNotFoundError:
        print(f"Error: the file {filename} was not found.")
        return None
    except Exception as e:
        print(f"Error occurred while reading {filename}: {e}")
        return 
    
# store the elements in variables
file = read_file(blueprint_filepath, blpnt_mode)
list = read_file(list_of_invitees_filepath, invt_mode)

# Set the counter of the letters 
tk = 1

# Loop for creating the list of personalized invitations
for name in list:
    invitation_letter = file.replace('[name]', name)
    # print(f"INVITEE N.{tk}")
    # print(invitation_letter)
    new_name = f'invitation_{name}.txt'
    filepath = os.path.join(output_dir, new_name) 
    with open(filepath, 'w') as f:
        f.write(invitation_letter)
    print(f"Invitation number {tk} for {name}: CREATED.")
    tk += 1


#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp